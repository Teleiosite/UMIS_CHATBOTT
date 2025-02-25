# init_db.py
from app import create_app, db  # Ensure these imports point to your correct app and db objects

app = create_app()

with app.app_context():
    db.create_all()  # Create tables for all models
    print("Database initialized!")
