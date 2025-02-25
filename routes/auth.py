"""
Authentication routes for student and admin users.
Handles login, signup, password changes, password recovery, and logout.
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from models.models import User, Admin, db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Handle student login with ID/email and password"""
    # Redirect authenticated users
    if current_user.is_authenticated:
        return redirect(url_for('chatbot.index'))

    # Process login form submission
    if request.method == 'POST':
        identifier = request.form.get('student_id').strip().lower()
        password = request.form.get('password')

        # Check both student ID and email
        user = User.query.filter_by(student_id=identifier).first()
        if not user:
            user = User.query.filter_by(email=identifier).first()

        # Validate credentials
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('chatbot.index'))

        flash('Invalid credentials', 'danger')
    return render_template('login.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """Handle new student registration"""
    if request.method == 'POST':
        # Validate form data
        student_id = request.form.get('student_id')
        email = request.form.get('email').lower().strip()
        password = generate_password_hash(request.form.get('password'))

        # Check for existing user
        if User.query.filter((User.student_id == student_id) | (User.email == email)).first():
            flash('User already exists', 'danger')
            return redirect(url_for('auth.signup'))

        # Create new user
        new_user = User(student_id=student_id, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! Please login', 'success')
        return redirect(url_for('auth.login'))

    return render_template('signup.html')

@auth_bp.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    """
    Handle in-app password changes for logged-in users.
    (This route requires the old password.)
    """
    if request.method == 'POST':
        old_password = request.form.get('old_password')
        new_password = generate_password_hash(request.form.get('new_password'))

        # Verify old password
        if check_password_hash(current_user.password, old_password):
            current_user.password = new_password
            db.session.commit()
            flash('Password updated successfully', 'success')
            return redirect(url_for('chatbot.index'))

        flash('Incorrect old password', 'danger')
    return render_template('change_password.html')

@auth_bp.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    """
    Handle password recovery using registered email.
    Users enter their registered email and new password (with confirmation).
    This route renders your existing change_password.html template.
    (Ensure the template is updated to include fields for email,
     new_password, and confirm_password—removing the old password field.)
    """
    if request.method == 'POST':
        email = request.form.get('email').strip().lower()
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("No account with that email was found", "danger")
            return redirect(url_for('auth.forgot_password'))
        if new_password != confirm_password:
            flash("Passwords do not match", "danger")
            return redirect(url_for('auth.forgot_password'))
        user.password = generate_password_hash(new_password)
        db.session.commit()
        flash("Password updated successfully. Please log in.", "success")
        return redirect(url_for('auth.login'))
    return render_template('change_password.html')

@auth_bp.route('/logout')
def logout():
    """Terminate user session"""
    logout_user()
    return redirect(url_for('auth.login'))

@auth_bp.route('/admin_login', methods=['GET', 'POST'])
def admin_login_page():
    """
    Handle admin login with username and password;
    redirect to dashboard upon success.
    """
    if current_user.is_authenticated:
        if isinstance(current_user, Admin):
            return redirect(url_for('admin.dashboard'))
        else:
            logout_user()  # Log out non-admin user
    if request.method == 'POST':
        admin_username = request.form.get('admin_username').strip()
        password = request.form.get('password')
        admin = Admin.query.filter_by(username=admin_username).first()
        if admin and check_password_hash(admin.password, password):
            login_user(admin)
            return redirect(url_for('admin.dashboard'))
        flash('Invalid admin credentials', 'danger')
    # Pass the signup URL so the admin login page can link to the signup page
    return render_template('admin_login.html', admin_signup_url=url_for('admin.admin_signup'))
