from flask import Flask
from flask_cors import CORS
from flask_session import Session
from models import db
from routes import bp

app = Flask(__name__)

# --- Config ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secretkey123'
app.config['SESSION_TYPE'] = 'filesystem'

# --- Init ---
CORS(app, supports_credentials=True)
Session(app)
db.init_app(app)

# --- Blueprints ---
app.register_blueprint(bp, url_prefix='/api')

# --- Run ---
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
