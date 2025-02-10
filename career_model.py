import os
from dotenv import load_dotenv
from together import Together

# Load environment variables from .env file
load_dotenv()

class CareerPathRecommender:
    def __init__(self):
        # Retrieve the API key from environment variables
        api_key = os.getenv('TOGETHER_AI_API_KEY')
        if not api_key:
            raise ValueError("API key must be set in the environment variables or .env file.")

        # Initialize the Together API client with the API key
        self.client = Together(api_key=api_key)

    def get_recommendations(self, pdf_data):
        # Prepare the messages for the API call
        messages = [
            {"role": "system", "content": "You are a PDF Reader."},
            {"role": "user", "content": (
                f"Analyze this PDF and set questions from this PDF. "
                f"For each career path, provide a brief description of relevant technologies, "
                f"you should write almost 10 questions that should be cover all PDF\n\n"
                f"Here is the PDF: {pdf_data}"
            )}
        ]

        try:
            # Make the API call to Together AI
            response = self.client.chat.completions.create(
                model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
                messages=messages,
                max_tokens=500,
                temperature=0.7,
                top_p=0.7,
                top_k=50,
                repetition_penalty=1,
                stop=["<|eot_id|>", "<|eom_id|>"],
                stream=False
            )

            
            # Return the response content
            return response.choices[0].message.content

        except AttributeError:
            return "Unexpected response format"
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

# Example usage (uncomment to test)
# recommender = CareerPathRecommender()
# recommendations = recommender.get_recommendations("John Doe, software engineer with experience in Python and machine learning.")
# print(recommendations)
