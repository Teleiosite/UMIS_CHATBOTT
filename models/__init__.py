"""
Initialize the SQLAlchemy database instance
This file ensures the database is accessible across all models
"""
from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy instance
db = SQLAlchemy()

# Import models after db initialization to avoid circular imports
from .models import User, Admin, FAQ