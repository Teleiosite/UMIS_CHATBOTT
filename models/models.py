"""
Database models for User, Admin, and FAQ entities
"""

from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from extensions import db  # Import the shared SQLAlchemy instance

class User(UserMixin, db.Model):
    """Student user model representing a standard user in the system."""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.student_id}>'

class Admin(UserMixin, db.Model):
    """Administrator model with elevated privileges."""
    __tablename__ = 'admins'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=True)

class FAQ(db.Model):
    """FAQ knowledge base entry with support for alternate phrasing of questions."""
    __tablename__ = 'faqs'
    
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    alternate_questions = db.Column(db.JSON)
