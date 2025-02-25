# create_admin.py
from models import db
from models.models import Admin
from werkzeug.security import generate_password_hash
from app import app  # Ensure this imports your Flask app

with app.app_context():
    # Check if an admin already exists to avoid duplicates
    if not Admin.query.first():
        admin = Admin(username="admin", password=generate_password_hash("Smart1234"))
        db.session.add(admin)
        db.session.commit()
        print("Admin account created!")
    else:
        print("Admin account already exists.")
