#GPT-Based Mock Interview

import openai 
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_mock_questions(career_path):
    prompt = f"Generate 5 mock interview questions for a {career_path}."
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
         messages=[
            {"role": "system", "content": "You are a helpful mock interview assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
