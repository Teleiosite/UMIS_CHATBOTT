import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from extensions import db  # Shared SQLAlchemy instance
from models.models import FAQ

app = create_app()

with app.app_context():
    # Create all tables if they don't exist
    db.create_all()
    print("Database tables created (if they didn't exist).")
    
    # Your FAQ data (replace with actual data)
  
    faq_data = [
    
    {
        "question": "How do I reset my UMIS portal password?",
        "alternate_questions": [
            "How can I reset my UMIS password?",
            "What's the process to reset my UMIS portal password?",
            "Steps to change UMIS password",
            "Password reset procedure for UMIS portal",
            "How to recover my UMIS account password?"
        ],
        "answer": "A:\n- Open the UMIS portal.\n- Click on \"Reset Password.\"\n- Enter your registered email.\n- Set your new password and confirm it.\n- Click \"Reset.\""
    },
    {
        "question": "How do I check my personal details on the UMIS portal?",
        "alternate_questions": [
            "How to view my personal information on UMIS?",
            "Where can I find my personal details in the UMIS portal?",
            "How do I access my personal info on UMIS?",
            "Viewing my profile information on UMIS",
            "Where are my personal details stored in UMIS?"
        ],
        "answer": "A:\n- Log in to the UMIS portal.\n- Navigate to the left-side navigation bar.\n- Click on \"Personal Details.\"\n\nClick this link to access the Personal Details page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=112:0"
    },
    {
        "question": "How do I check my examination results?",
        "alternate_questions": [
            "How to view my exam grades?",
            "Where do I find my semester results?",
            "How do I see my examination scores on UMIS?",
            "Accessing my academic results on UMIS",
            "Where are my test scores displayed in UMIS?"
        ],
        "answer": "A:\n- Log in to the UMIS portal.\n- Click on \"Academic Details\" in the navigation bar.\n- Click on \"Semester Results.\"\n\nClick this link to access the Semester Results page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=19:0\n- Select the semester you want to view."
    },
    {
        "question": "How do I check my unofficial transcript?",
        "alternate_questions": [
            "How can I get my unofficial transcript?",
            "Where to find my academic transcript on UMIS?",
            "Accessing unofficial transcript steps",
            "Viewing my temporary academic record",
            "How to download my UMIS transcript?"
        ],
        "answer": "A:\n- Log in to the UMIS portal.\n- Click on \"Academic Details.\"\n- Select \"Unofficial Transcript.\"\n\nClick this link to access the Unofficial Transcript page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=21:0"
    },
    {
        "question": "How do I check my checklisting status?",
        "alternate_questions": [
            "How to see my checklisting status?",
            "Where is the checklisting information located?",
            "How do I verify my checklisting status?",
            "Checking my academic checklist completion",
            "Viewing course checklist progress"
        ],
        "answer": "A:\n- Log in to the UMIS portal.\n- Click on \"Academic Details.\"\n- Select \"Check Listing.\"\n\nClick this link to access the Check Listing page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=26:0"
    },
    {
        "question": "How do I commence my course registration?",
        "alternate_questions": [
            "How to start course registration?",
            "Beginning course registration process",
            "Steps to register for courses",
            "How do I start selecting my classes?",
            "Initiating course selection on UMIS"
        ],
        "answer": "A:\n- Log in to the UMIS portal.\n- Click on \"Course Selection.\"\n- Select \"Commence Registration.\"\n\nClick this link to access the Course Registration page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=22:0\n- Follow the prompts to select your courses."
    },
    {
        "question": "What should I do if I encounter an error during course registration?",
        "alternate_questions": [
            "Troubleshooting course registration errors",
            "How to fix registration errors?",
            "What if I get an error while registering?",
            "Course registration problem solution",
            "Who to contact for registration issues?"
        ],
        "answer": "A:\nContact your course advisor for assistance."
    },
    {
        "question": "How do I add or drop a course after registration?",
        "alternate_questions": [
            "Changing course selections post-registration",
            "How to modify my registered courses?",
            "Adding/dropping classes after deadline",
            "Course adjustment procedure",
            "Updating my course selections"
        ],
        "answer": "A:\n**To add a course:**\n- Click on \"Course Selection.\"\n- Select \"Select Courses.\"\n\nClick this link to access the Select Courses page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=24:0\n- Scan for the course you want to add.\n- Click the checkbox beside the course and lecturer.\n\n**To drop a course:**\n- Go to \"Selected Course List.\"\n\nClick this link to access the Selected Course List page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=27:0\n- Scroll to the bottom of the page.\n- Click the \"Apply to Drop\" button."
    },
    {
        "question": "How do I check my outstanding courses?",
        "alternate_questions": [
            "Viewing incomplete courses",
            "How to see remaining required courses?",
            "Checking uncompleted classes",
            "Finding pending course requirements",
            "Where to find outstanding courses?"
        ],
        "answer": "A:\n- Log in to UMIS.\n- Navigate to \"Course Selection.\"\n- Click on \"Outstanding Courses.\"\n\nClick this link to access the Outstanding Courses page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=103:0"
    },
    {
        "question": "How do I know if I have an outstanding course to retake?",
        "alternate_questions": [
            "Identifying courses needing retake",
            "How to check failed courses?",
            "Finding courses marked for repetition",
            "Checking required retakes",
            "Viewing incomplete course status"
        ],
        "answer": "A:\n- Go to \"Check Listing\" under \"Academic Details.\"\n- Look for courses marked as \"NO.\""
    },
    {
        "question": "How do I view my class timetable?",
        "alternate_questions": [
            "Accessing my schedule",
            "Where to find class schedule?",
            "Checking course timetable",
            "Viewing class times and locations",
            "How to see my daily schedule?"
        ],
        "answer": "A:\n- Log in to UMIS.\n- Click \"Course Selection.\"\n- Select \"Current Timetable.\"\n\nClick this link to access the Current Timetable page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=12:0"
    },
    {
        "question": "How do I check my selected timetable?",
        "alternate_questions": [
            "Viewing chosen schedule",
            "Accessing finalized timetable",
            "Checking registered class times",
            "Where to see selected schedule?",
            "How to review my chosen timetable?"
        ],
        "answer": "A:\n- Log in to UMIS.\n- Click \"Course Selection.\"\n- Select \"Selected Timetable.\"\n\nClick this link to access the Selected Timetable page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=12:0"
    },
    {
        "question": "How do I check my registration status?",
        "alternate_questions": [
            "Verifying registration completion",
            "Where to check registration status?",
            "Confirming registration is finalized",
            "How to know if I'm fully registered?",
            "Viewing enrollment confirmation"
        ],
        "answer": "A:\n- Click on \"Finance.\"\n- Select \"Check Registration Status.\"\n\nClick this link to access the Registration Status page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=30:0"
    },
    {
        "question": "Where can I check my GPA and CGPA?",
        "alternate_questions": [
            "How to find my GPA/CGPA?",
            "Viewing academic performance metrics",
            "Checking grade point averages",
            "Where are GPA results displayed?",
            "Accessing cumulative GPA information"
        ],
        "answer": "A:\n- Click on \"Academic Details.\"\n- Select \"Semester Results.\"\n- Your GPA for each semester and cumulative CGPA will be displayed."
    },
    {
        "question": "How do I access my past academic results?",
        "alternate_questions": [
            "Viewing historical grades",
            "Checking previous semester results",
            "Accessing archived academic records",
            "How to see old exam scores?",
            "Finding past academic performance"
        ],
        "answer": "A:\n- Click on \"Academic Details.\"\n- Select \"Semester Results.\"\n\nClick this link to access the Semester Results page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=19:0\n- Choose the semester result you want to view."
    },
    {
        "question": "How do I check my finance statement?",
        "alternate_questions": [
            "Viewing financial account summary",
            "Accessing payment history",
            "Checking tuition fee statements",
            "Where to find financial records?",
            "How to see my financial transactions?"
        ],
        "answer": "A:\n- Log in to UMIS.\n- Click on \"Finance.\"\n- Select \"Finance Statement.\"\n\nClick this link to access the Finance Statement page: https://umis.babcock.edu.ng/babcock/a_statement.jsp?view=33:0"
    },
    {
        "question": "How do I make online payments for tuition and other fees?",
        "alternate_questions": [
            "Paying fees through UMIS",
            "Online tuition payment process",
            "Steps for electronic payments",
            "How to pay school fees online?",
            "Completing fee payments digitally"
        ],
        "answer": "A:\n- Complete your hall, church, and meal plan registration.\n- Click \"Submit Registration.\"\n- Go to \"Finance\" → \"Current Charges.\"\n\nClick this link to access the Current Charges page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=33:0\n- Click \"Go\" to see the total amount.\n- Click \"Make Payments\" → \"eTranzact.\"\n- Pay the stated amount for the semester."
    },
    {
        "question": "Can I view my payment history on UMIS?",
        "alternate_questions": [
            "Checking past payments",
            "Viewing transaction history",
            "Accessing payment records",
            "How to see previous fee payments?",
            "Where is payment history stored?"
        ],
        "answer": "A:\n- Go to \"Finance.\"\n- Click \"Current Charges.\"\n\nClick this link to access the Current Charges page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=33:0\n- Select \"Completed Charges.\"\n\nClick this link to access the Completed Charges page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=33:0:2&data=514388"
    },
    {
        "question": "What should I do if my payment is not reflecting on UMIS?",
        "alternate_questions": [
            "Troubleshooting missing payments",
            "Payment not showing in system",
            "Resolving payment verification issues",
            "Unrecognized transaction resolution",
            "Payment confirmation problems"
        ],
        "answer": "A:\n- Contact the Bursary Department for assistance."
    },
    {
        "question": "How do I generate my school fees invoice?",
        "alternate_questions": [
            "Creating payment receipt",
            "Printing fee invoice",
            "Generating tuition bill",
            "How to get payment documentation?",
            "Producing official fee statement"
        ],
        "answer": "A:\n- Click on \"Finance.\"\n- Go to \"Current Charges.\"\n\nClick this link to access the Current Charges page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=33:0\n- Click \"Receipt.\"\n\nClick this link to access the Receipt page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=33:0"
    },
    {
        "question": "Can I pay my tuition fees in installments?",
        "alternate_questions": [
            "Partial tuition payments",
            "Split payment options",
            "Installment plan availability",
            "Paying fees in multiple transactions",
            "Divided payment arrangements"
        ],
        "answer": "A:\n- I’m not sure. Please contact the Bursary Department for clarification."
    },
    {
        "question": "How do I print my course form?",
        "alternate_questions": [
            "Generating course registration document",
            "Printing class selection form",
            "Exporting course registration PDF",
            "How to get official course list?",
            "Downloading registration confirmation"
        ],
        "answer": "A:\n- Go to \"Finance.\"\n- Click \"Print Course Form.\"\n\nClick this link to access the Print Course Form page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=50:0\n- Download and print the document."
    },
    {
        "question": "How do I register for a previous semester?",
        "alternate_questions": [
            "Backdating semester registration",
            "Registering for past terms",
            "Late enrollment for previous semesters",
            "How to complete old registrations?",
            "Catching up on missed registration"
        ],
        "answer": "A:\n- Click on \"Finance.\"\n- Select \"Register Previous Semester.\"\n\nClick this link to access the Register Previous Semester page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=44:0\n- Follow the instructions to complete registration."
    },
    {
        "question": "How do I print previous course form?",
        "alternate_questions": [
            "How to get past course forms?",
            "Printing old registration documents",
            "Accessing previous semester course forms",
            "How to download earlier course registration forms?",
            "Retrieving historical course forms from UMIS"
        ],
        "answer": "A:\n- Go to \"Finance.\"\n- Click \"Print Course Form.\"\n\nClick this link to access the Print Course Form page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=50:0\n- Then click on previous course form:\n\nClick this link to access the Previous Course Form page: https://umis.babcock.edu.ng/babcock/a_students.jsp?view=50:1&data=\n- Download and print the document."
    }
]  
    
    # Function to populate FAQs
    def populate_faqs():
        for faq in faq_data:
            new_faq = FAQ(
                question=faq["question"],
                answer=faq["answer"],
                alternate_questions=faq["alternate_questions"]
            )
            db.session.add(new_faq)
        db.session.commit()
        print("Successfully populated FAQs!")
    
    if __name__ == "__main__":
        populate_faqs()
