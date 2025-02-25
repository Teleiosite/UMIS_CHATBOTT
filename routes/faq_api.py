"""
FAQ JSON API endpoints for CRUD operations
Used by the admin dashboard and chatbot interface
"""
from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models.models import FAQ, db

faq_api = Blueprint('faq_api', __name__)

@faq_api.route('/api/faqs', methods=['GET'])
def get_faqs():
    """
    Fetch all FAQs as JSON
    Used by the admin dashboard and chatbot interface
    """
    faqs = FAQ.query.all()
    return jsonify([{
        'id': f.id,
        'question': f.question,
        'answer': f.answer,
        'alternate_questions': f.alternate_questions
    } for f in faqs])

@faq_api.route('/api/faqs/<int:faq_id>', methods=['GET'])
def get_faq(faq_id):
    """
    Fetch a single FAQ by ID
    Args:
        faq_id (int): The ID of the FAQ to retrieve
    """
    faq = FAQ.query.get_or_404(faq_id)
    return jsonify({
        'id': faq.id,
        'question': faq.question,
        'answer': faq.answer,
        'alternate_questions': faq.alternate_questions
    })

@faq_api.route('/api/faqs', methods=['POST'])
@login_required
def create_faq():
    """
    Create a new FAQ entry
    Requires admin authentication
    """
    if not current_user.is_admin:
        return jsonify({"error": "Unauthorized"}), 403
    
    data = request.get_json()
    new_faq = FAQ(
        question=data['question'],
        answer=data['answer'],
        alternate_questions=data.get('alternate_questions', [])
    )
    db.session.add(new_faq)
    db.session.commit()
    return jsonify({"message": "FAQ created", "id": new_faq.id}), 201

@faq_api.route('/api/faqs/<int:faq_id>', methods=['PUT'])
@login_required
def update_faq(faq_id):
    """
    Update an existing FAQ
    Args:
        faq_id (int): The ID of the FAQ to update
    """
    if not current_user.is_admin:
        return jsonify({"error": "Unauthorized"}), 403
    
    faq = FAQ.query.get_or_404(faq_id)
    data = request.get_json()
    
    faq.question = data.get('question', faq.question)
    faq.answer = data.get('answer', faq.answer)
    faq.alternate_questions = data.get('alternate_questions', faq.alternate_questions)
    
    db.session.commit()
    return jsonify({"message": "FAQ updated"})

@faq_api.route('/api/faqs/<int:faq_id>', methods=['DELETE'])
@login_required
def delete_faq(faq_id):
    """
    Delete an FAQ entry
    Args:
        faq_id (int): The ID of the FAQ to delete
    """
    if not current_user.is_admin:
        return jsonify({"error": "Unauthorized"}), 403
    
    faq = FAQ.query.get_or_404(faq_id)
    db.session.delete(faq)
    db.session.commit()
    return jsonify({"message": "FAQ deleted"})