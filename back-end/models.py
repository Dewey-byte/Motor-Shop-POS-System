from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
# Initialize SQLAlchemy
db = SQLAlchemy()


# ============================
# User Model
# ============================
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(200))
    role = db.Column(db.String(50), default='cashier')  # can be 'admin' or 'cashier'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# ============================
# Supplier Model
# ============================
class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    contact = db.Column(db.String(200))
    address = db.Column(db.Text)

# ============================
# Customer Model
# ============================
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(50))
    email = db.Column(db.String(120))
    address = db.Column(db.Text)

# ============================
# Category Model
# ============================
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

# ============================
# Product Model
# ============================
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    cost = db.Column(db.Numeric(10, 2), default=0)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, default=0)
    reorder_level = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    category = db.relationship('Category', backref='products', lazy=True)
    supplier = db.relationship('Supplier', backref='products', lazy=True)

# ============================
# Sale Model
# ============================
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_no = db.Column(db.String(50), unique=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    total_amount = db.Column(db.Numeric(12, 2), nullable=False)
    payment_method = db.Column(db.Enum('cash', 'card', 'other'), default='cash')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    customer = db.relationship('Customer', backref='sales', lazy=True)
    user = db.relationship('User', backref='sales', lazy=True)
    items = db.relationship('SaleItem', backref='sale', cascade='all, delete-orphan', lazy=True)

# ============================
# SaleItem Model
# ============================
class SaleItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)
    subtotal = db.Column(db.Numeric(12, 2), nullable=False)

    # Relationship
    product = db.relationship('Product', backref='sale_items', lazy=True)
