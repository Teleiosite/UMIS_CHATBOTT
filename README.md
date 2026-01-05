# Babcock University UMIS Chatbot

This project is a web-based chatbot designed to assist Babcock University students by providing instant answers to frequently asked questions about the University's Unified Management Information System (UMIS). The chatbot aims to streamline access to information regarding course registration, fee payment, academic records, and other common UMIS functionalities.

## Features

*   **Conversational Interface:** A user-friendly chat interface for students to ask questions in natural language.
*   **Comprehensive FAQ Database:** Pre-populated with a wide range of questions and answers related to:
    *   Course Registration (checking status, outstanding courses, course selection)
    *   Fee Payment (payment procedures, viewing history)
    *   Academic Records (checking results, GPA, checklists)
*   **User Authentication:** Secure signup and login functionality for students.
*   **Admin Dashboard:** A protected administrative panel for managing the chatbot's knowledge base. Admins can:
    *   View all FAQs.
    *   Add new question-and-answer pairs.
    *   Edit existing FAQs to keep information up-to-date.
    *   Delete irrelevant or outdated FAQs.
*   **Smart Query Matching:** Utilizes Natural Language Processing (NLP) techniques to understand and match user questions to the most relevant answers in the database.

## Getting Started

Follow these instructions to get a local copy of the project up and running.

### Prerequisites

*   Python 3.8 or higher
*   pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Babcock-UMIS-Chatbot.git
    cd Babcock-UMIS-Chatbot
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Database Setup

1.  **Initialize the database:**
    This will create the necessary tables for the application.
    ```bash
    python init_db.py
    ```

2.  **Populate the database with FAQs:**
    This script will populate the `faq` table with a predefined set of questions and answers.
    ```bash
    python scripts/populate_faqs.py
    ```

### Running the Application

1.  **Start the Flask development server:**
    ```bash
    flask run
    ```
2.  Open your web browser and navigate to `http://127.0.0.1:5000` to access the chatbot.

## Usage

### Student User

1.  Navigate to the homepage.
2.  Sign up for a new account or log in with existing credentials.
3.  Use the chat interface to ask questions about UMIS (e.g., "How do I register my courses?", "How can I check my results?").

### Admin User

1.  To create an admin account, run the following command and follow the prompts:
    ```bash
    python scripts/create_admin.py
    ```
2.  Navigate to the admin login page: `http://127.0.0.1:5000/admin/login`.
3.  Log in with your admin credentials to access the dashboard.
4.  From the dashboard, you can add, edit, or delete FAQs to manage the chatbot's knowledge base.

## Project Structure

```
.
├── app.py                  # Main Flask application file
├── config.py               # Configuration settings
├── requirements.txt        # Project dependencies
├── chatbot.db              # SQLite database file
├── init_db.py              # Script to initialize the database
├── extensions.py           # Flask extensions setup
├── models/                 # SQLAlchemy database models
│   ├── __init__.py
│   └── models.py
├── routes/                 # Flask blueprint routes
│   ├── __init__.py
│   ├── admin.py            # Admin-related routes
│   ├── auth.py             # Authentication routes
│   ├── chatbot.py          # Chatbot interaction routes
│   └── faq_api.py          # API for FAQ management
├── scripts/                # Utility scripts
│   ├── create_admin.py     # Script to create an admin user
│   └── populate_faqs.py    # Script to populate the FAQ database
├── static/                 # Static assets (CSS, JavaScript, Images)
│   ├── script.js
│   └── styles.css
├── templates/              # HTML templates
│   ├── admin_login.html
│   ├── dashboard.html
│   ├── edit_faq.html
│   └── ...
└── utilities/              # Core application logic
    └── chatbot_logic.py    # NLP and response generation logic
```

## Technologies Used

*   **Backend:** Python, Flask
*   **Database:** SQLite with SQLAlchemy ORM
*   **NLP:**
    *   **spaCy:** For natural language understanding.
    *   **FuzzyWuzzy:** For flexible string matching.
*   **Frontend:** HTML, CSS, JavaScript
*   **Authentication:** Flask-Login
