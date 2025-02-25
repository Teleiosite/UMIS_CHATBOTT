from flask import Flask
from flask_login import LoginManager
from config import Config
from routes.faq_api import faq_api
from extensions import db  # Import the shared SQLAlchemy instance

# Initialize the login manager
login_manager = LoginManager()

def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    # Create a new Flask application instance
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration settings

    # Initialize extensions with the app instance
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Set the default login view

    # Import models after app and db have been set up
    from models.models import User, Admin

    @login_manager.user_loader
    def load_user(user_id):
        """
        Load a user from the database by ID.
        Checks both User and Admin tables.
        """
        user = User.query.get(int(user_id))
        return user or Admin.query.get(int(user_id))

    # Register blueprints for different modules
    from routes.auth import auth_bp
    from routes.admin import admin_bp
    from routes.chatbot import chatbot_bp

    app.register_blueprint(auth_bp)               # Authentication routes
    app.register_blueprint(admin_bp, url_prefix='/admin')  # Admin panel routes
    app.register_blueprint(chatbot_bp)              # Chatbot routes
    app.register_blueprint(faq_api, url_prefix='/api')  # FAQ API routes

    return app  # Return the configured app instance

if __name__ == "__main__":
    # Create the app instance
    app = create_app()

    # Ensure the app context is active and initialize the database
    with app.app_context():
        db.create_all()  # Create database tables for all models
        print("Database initialized!")

    # Run the app in debug mode
    app.run(debug=True)
