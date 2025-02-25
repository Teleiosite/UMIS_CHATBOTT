"""
Script to create an admin account from the command line
Usage: python create_admin.py <username> <password>
"""
import sys
from werkzeug.security import generate_password_hash
from models.models import Admin, db
from app import create_app

def create_admin(username, password):
    """
    Create a new admin account
    Args:
        username (str): Admin login name
        password (str): Plaintext password (will be hashed)
    """
    app = create_app()
    with app.app_context():
        # Check if admin already exists
        if Admin.query.filter_by(username=username).first():
            print(f"Admin '{username}' already exists!")
            return
        
        # Create new admin
        new_admin = Admin(
            username=username,
            password=generate_password_hash(password),
            is_admin=True
        )
        db.session.add(new_admin)
        db.session.commit()
        print(f"Admin '{username}' created successfully!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_admin.py <username> <password>")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    create_admin(username, password)