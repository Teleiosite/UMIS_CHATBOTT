import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev_key_123')

    # Check for PythonAnywhere specific environment variables
    if 'PA_DB_HOST' in os.environ:
        username = os.getenv('PA_DB_USER')
        password = os.getenv('PA_DB_PASSWORD')
        hostname = os.getenv('PA_DB_HOST')
        databasename = os.getenv('PA_DB_NAME')
        
        # Construct the MySQL connection string
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{username}:{password}@{hostname}/{databasename}"
    else:
        # Fallback to SQLite for local development
        SQLALCHEMY_DATABASE_URI = 'sqlite:///chatbot.db'
        
    SQLALCHEMY_TRACK_MODIFICATIONS = False