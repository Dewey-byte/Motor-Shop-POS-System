from flask import Blueprint, request, jsonify, session
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Product, Sale, SaleItem, User  # ✅ works if __init__.py exists

bp = Blueprint('api', __name__)

# ============================
# Authentication
# ============================
@bp.route('/auth/login', methods=['POST'])
def login():
    data = request.json or {}
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    u = User.query.filter_by(username=username).first()
    if not u or not u.check_password(password):
        return jsonify({'error': 'Invalid credentials'}), 401

    # Save user info in session
    session['user_id'] = u.id
    session['username'] = u.username
    session['role'] = u.role

    return jsonify({'id': u.id, 'username': u.username, 'role': u.role})


@bp.route('/auth/logout', methods=['POST'])
def logout():
    session.clear()
    return ('', 204)


@bp.route('/auth/whoami', methods=['GET'])
def whoami():
    if 'user_id' not in session:
        return jsonify({'user': None})
    return jsonify({
        'user': {
            'id': session.get('user_id'),
            'username': session.get('username'),
            'role': session.get('role')
        }
    })


# ============================
# Products
# ============================
@bp.route('/products', methods=['GET'])
def list_products():
    q = request.args.get('q')
    if q:
        items = Product.query.filter(
            (Product.name.ilike(f'%{q}%')) | (Product.sku.ilike(f'%{q}%'))
        ).limit(50).all()
    else:
        items = Product.query.limit(100).all()

    return jsonify([
        {'id': p.id, 'sku': p.sku, 'name': p.name, 'price': str(p.price), 'stock': p.stock}
        for p in items
    ])


@bp.route('/products', methods=['POST'])
def create_product():
    data = request.json or {}
    p = Product(
        sku=data.get('sku'),
        name=data.get('name'),
        price=data.get('price') or 0,
        stock=data.get('stock', 0)
    )
    db.session.add(p)
    db.session.commit()
    return jsonify({'id': p.id}), 201


@bp.route('/scan/<sku>', methods=['GET'])
def scan_sku(sku):
    p = Product.query.filter_by(sku=sku).first()
    if not p:
        return jsonify({'error': 'not found'}), 404
    return jsonify({
        'id': p.id,
        'sku': p.sku,
        'name': p.name,
        'price': str(p.price),
        'stock': p.stock
    })


# ============================
# Sales
# ============================
@bp.route('/sales', methods=['POST'])
def create_sale():
    data = request.json or {}
    items = data.get('items') or []
    if not items:
        return jsonify({'error': 'no items'}), 400

    try:
        total = sum([float(i['qty']) * float(i['unit_price']) for i in items])
    except Exception:
        return jsonify({'error': 'invalid items format'}), 400

    invoice_no = 'INV-' + datetime.utcnow().strftime('%Y%m%d%H%M%S')
    sale = Sale(
        invoice_no=invoice_no,
        customer_id=data.get('customer_id'),
        user_id=session.get('user_id'),
        total_amount=total,
        payment_method=data.get('payment_method', 'cash')
    )

    db.session.add(sale)
    db.session.flush()

    for it in items:
        si = SaleItem(
            sale_id=sale.id,
            product_id=it['product_id'],
            qty=int(it['qty']),
            unit_price=it['unit_price'],
            subtotal=float(it['qty']) * float(it['unit_price'])
        )

        prod = Product.query.get(it['product_id'])
        if prod:
            prod.stock = (prod.stock or 0) - int(it['qty'])
            db.session.add(prod)

        db.session.add(si)

    db.session.commit()
    return jsonify({'sale_id': sale.id, 'invoice_no': invoice_no}), 201


# ============================
# Simple Health Check
# ============================
@bp.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


@bp.route('/')
def home():
    return jsonify({"message": "POS API is running!"})

@bp.route('/register', methods=['POST'])
def register():
    data = request.json or {}
    username = data.get('username')
    password = data.get('password')
    full_name = data.get('full_name')

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400

    u = User(username=username, full_name=full_name)
    u.set_password(password)
    db.session.add(u)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201
