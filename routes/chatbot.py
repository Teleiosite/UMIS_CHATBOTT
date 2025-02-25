from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from models.models import FAQ
from fuzzywuzzy import fuzz
import json
import spacy

# Create a blueprint for chatbot routes
chatbot_bp = Blueprint('chatbot', __name__)

# Load spaCy's English model (ensure it's downloaded: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

@chatbot_bp.route('/')
@login_required
def index():
    # Render the main chatbot interface (index.html)
    return render_template('index.html')

@chatbot_bp.route('/chat', methods=['POST'])
@login_required
def chat():
    try:
        # Debug: Indicate that the chat endpoint has been reached
        print("Chat endpoint hit")
        
        # Retrieve JSON data from the request
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        # Return a message if the user_message is empty
        if not user_message:
            return jsonify({'response': "Please enter a valid message."})
        
        # Normalize the user's message (convert to lowercase) and create a spaCy document
        doc_query = nlp(user_message.lower())
        
        # Retrieve all FAQ entries from the database
        faqs = FAQ.query.all()
        best_match = None
        highest_score = 0
        
        # Set a matching threshold (adjust as needed)
        threshold = 50

        # Loop through each FAQ entry to calculate similarity scores
        for faq in faqs:
            # Normalize the main FAQ question
            main_question = faq.question.strip().lower()
            faq_doc = nlp(main_question)
            spacy_score = doc_query.similarity(faq_doc) * 100  # Scale spaCy score to 0-100
            fuzzy_score = fuzz.partial_ratio(user_message.lower(), main_question)
            combined_score = (spacy_score + fuzzy_score) / 2

            # Debug: Print computed scores for the FAQ
            print(f"FAQ: '{main_question}' - SpaCy Score: {spacy_score:.2f}, Fuzzy Score: {fuzzy_score}, Combined Score: {combined_score:.2f}")
            
            # Check if alternate questions exist and calculate scores for them
            if faq.alternate_questions:
                try:
                    alt_qs = json.loads(faq.alternate_questions)
                except Exception:
                    alt_qs = []
                for alt in alt_qs:
                    alt_normalized = alt.strip().lower()
                    alt_doc = nlp(alt_normalized)
                    spacy_alt_score = doc_query.similarity(alt_doc) * 100
                    fuzzy_alt_score = fuzz.partial_ratio(user_message.lower(), alt_normalized)
                    combined_alt_score = (spacy_alt_score + fuzzy_alt_score) / 2
                    if combined_alt_score > combined_score:
                        combined_score = combined_alt_score

            # Update best match if this FAQ has a higher combined score
            if combined_score > highest_score:
                highest_score = combined_score
                best_match = faq

        # Determine the response based on the highest score and threshold
        if best_match and highest_score >= threshold:
            response = best_match.answer
        else:
            response = "I'm sorry, I don't understand your question. Could you please rephrase?"
        
        # Debug: Print the final response
        print("Chat response:", response)
        return jsonify({'response': response})
    except Exception as e:
        # Log any errors that occur during processing
        print("Error in chat endpoint:", e)
        return jsonify({'response': "An error occurred while processing your request."}), 500

@chatbot_bp.route('/api/faqs', methods=['GET'])
@login_required
def get_faqs():
    try:
        # Retrieve all FAQs from the database
        faqs = FAQ.query.all()
        result = []
        for faq in faqs:
            try:
                alt_questions = json.loads(faq.alternate_questions) if faq.alternate_questions else []
            except Exception:
                alt_questions = []
            result.append({
                "id": faq.id,
                "question": faq.question,
                "alternate_questions": alt_questions,
                "answer": faq.answer
            })
        return jsonify(result)
    except Exception as e:
        print("Error in get_faqs:", e)
        return jsonify({"error": "An error occurred while fetching FAQs."}), 500
