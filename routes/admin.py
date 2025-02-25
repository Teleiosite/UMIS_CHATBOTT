"""
Admin management routes for:
- Dashboard access
- FAQ CRUD operations
- Admin user management
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models.models import FAQ, Admin, db
from flask_login import login_required, current_user

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


def ensure_admin():
    """Middleware to verify admin privileges"""
    if not current_user.is_authenticated or not isinstance(current_user, Admin):
        flash("Admin access required", "danger")
        return False
    return True


@admin_bp.route('/dashboard')
@login_required
def dashboard():
    """Admin control panel showing FAQ list and stats"""
    if not ensure_admin():
        return redirect(url_for('auth.admin_login_page'))

    # Get all FAQs for display
    faqs = FAQ.query.all()
    return render_template('dashboard.html', faqs=faqs)


@admin_bp.route('/api/faqs', methods=['GET', 'POST'])
def faqs_api():
    """
    GET: Return all FAQs as JSON.
    POST: Create a new FAQ.
    """
    if request.method == 'GET':
        faqs = FAQ.query.all()
        return jsonify([{
            'id': f.id,
            'question': f.question,
            'answer': f.answer,
            'alternate_questions': f.alternate_questions
        } for f in faqs])
    elif request.method == 'POST':
        data = request.get_json()
        question = data.get('question')
        answer = data.get('answer')
        alternate_questions = data.get('alternate_questions', '')
        if not question or not answer:
            return jsonify({'message': 'Question and answer required'}), 400
        new_faq = FAQ(question=question, answer=answer, alternate_questions=alternate_questions)
        db.session.add(new_faq)
        db.session.commit()
        return jsonify({'message': 'FAQ created successfully'}), 201


@admin_bp.route('/api/faqs/<int:faq_id>', methods=['PUT', 'DELETE'])
def faq_detail_api(faq_id):
    """
    PUT: Update an FAQ.
    DELETE: Delete an FAQ.
    """
    faq = FAQ.query.get_or_404(faq_id)
    if request.method == 'PUT':
        data = request.get_json()
        faq.question = data.get('question', faq.question)
        faq.answer = data.get('answer', faq.answer)
        faq.alternate_questions = data.get('alternate_questions', faq.alternate_questions)
        db.session.commit()
        return jsonify({'message': 'FAQ updated successfully'}), 200
    elif request.method == 'DELETE':
        db.session.delete(faq)
        db.session.commit()
        return jsonify({'message': 'FAQ deleted successfully'}), 200


@admin_bp.route('/faqs/edit/<int:faq_id>', methods=['GET', 'POST'])
@login_required
def edit_faq(faq_id):
    """Route for editing an FAQ via a form (for non-AJAX requests)"""
    if not ensure_admin():
        return redirect(url_for('auth.admin_login_page'))
    faq = FAQ.query.get_or_404(faq_id)
    if request.method == 'POST':
        faq.question = request.form.get('question')
        faq.alternate_questions = request.form.get('alternate_questions')
        faq.answer = request.form.get('answer')
        try:
            db.session.commit()
            flash('FAQ updated successfully', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error updating FAQ: ' + str(e), 'danger')
        return redirect(url_for('admin.dashboard'))
    return render_template('edit_faq.html', faq=faq)


@admin_bp.route('/admin_signup', methods=['GET', 'POST'])
def admin_signup():
    """Route for creating a new admin account.
       After successful signup, the admin is redirected to the admin login page.
    """
    if request.method == 'POST':
        admin_username = request.form.get('admin_username')
        password_raw = request.form.get('password')
        if not admin_username or not password_raw:
            flash('All fields are required', 'danger')
            return redirect(url_for('admin.admin_signup'))
        existing_admin = Admin.query.filter_by(username=admin_username).first()
        if existing_admin:
            flash('An admin account with that username already exists', 'danger')
            return redirect(url_for('admin.admin_signup'))
        password = generate_password_hash(password_raw)
        new_admin = Admin(username=admin_username, password=password)
        db.session.add(new_admin)
        db.session.commit()
        flash('Admin account created successfully', 'success')
        return redirect(url_for('auth.admin_login_page'))
    return render_template('admin_signup.html')
