# create_admin.py
from app import app
from models import db, User

def create_admin():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    full_name = input("Enter full name (optional): ")

    with app.app_context():
        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            print("⚠️  User already exists!")
            return

        # Create new admin user
        admin = User(
            username=username,
            full_name=full_name,
            role='admin'
        )
        admin.set_password(password)

        db.session.add(admin)
        db.session.commit()

        print(f"✅ Admin user created successfully!")
        print(f"👤 Username: {username}")
        print(f"🧩 Role: admin")

if __name__ == "__main__":
    create_admin()
