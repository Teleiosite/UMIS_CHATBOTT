"""
FAQ matching logic using fuzzy string matching and semantic similarity
"""
from fuzzywuzzy import fuzz  # For string similarity comparisons
import spacy                 # For NLP-based semantic analysis

# Load medium-sized English language model for best performance
nlp = spacy.load("en_core_web_md")

def get_best_faq_match(user_query, faqs, threshold=75):
    """
    Find the best matching FAQ entry using combined scoring:
    - 60% fuzzy string matching (handles typos and variations)
    - 40% semantic similarity (understands meaning)
    
    Args:
        user_query (str): The student's question
        faqs (list): FAQ database entries
        threshold (int): Minimum match score (0-100)
    
    Returns:
        str: Best matching answer or default message
    """
    best_match = None
    max_score = 0
    
    for faq in faqs:
        # Fuzzy match scores
        main_score = fuzz.token_set_ratio(user_query, faq.question)
        alt_scores = [fuzz.token_set_ratio(user_query, alt_q) for alt_q in faq.alternate_questions]
        max_alt_score = max(alt_scores) if alt_scores else 0
        fuzzy_score = max(main_score, max_alt_score)
        
        # Semantic similarity score
        doc1 = nlp(user_query)
        doc2 = nlp(faq.question)
        semantic_score = doc1.similarity(doc2) * 100
        
        # Combined weighted score
        combined_score = fuzzy_score * 0.6 + semantic_score * 0.4
        
        # Update best match if threshold met
        if combined_score > max_score and combined_score >= threshold:
            max_score = combined_score
            best_match = faq.answer
    
    return best_match if best_match else "I don't understand. Could you rephrase your question?"