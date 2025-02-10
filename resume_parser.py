import pdfplumber
import re
import random

def extract_sentences_from_pdf(pdf_path):
    """Extract sentences from a PDF file."""
    text_data = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                sentences = re.split(r'(?<=[.!?])\s+', text)  # Split text into sentences
                text_data.extend(sentences)
    
    return text_data

def generate_questions(sentences):
    """Generate 10 questions from extracted sentences."""
    questions = []
    
    for sentence in sentences:
        words = sentence.split()
        if len(words) > 5:  # Only consider meaningful sentences
            question_type = random.choice(["what", "why", "how", "explain", "list"])
            
            if question_type == "what":
                question = f"What is {words[0]}?"
            elif question_type == "why":
                question = f"Why is {words[1]} important?"
            elif question_type == "how":
                question = f"How does {words[0]} work?"
            elif question_type == "explain":
                question = f"Explain {words[0]} in detail."
            elif question_type == "list":
                question = f"List the key points about {words[0]}."
            
            questions.append(question)

            if len(questions) >= 10:  # Stop after 10 questions
                break

    return questions

def extract_questions_from_pdf(pdf_path):
    """Main function to extract and generate questions from a PDF."""
    sentences = extract_sentences_from_pdf(pdf_path)
    
    if not sentences:
        return ["No text found in PDF."]
    
    questions = generate_questions(sentences)
    
    return questions if questions else ["Could not generate questions."]

# Example usage (uncomment to test)
# pdf_path = "sample.pdf"  # Replace with actual PDF file path
# questions = extract_questions_from_pdf(pdf_path)
# for q in questions:
#     print(q)
