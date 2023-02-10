import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key=os.getenv('OPENAI_API_KEY')

print("Calling GPT3")
response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(""),
            max_tokens=4000,
            frequency_penalty=1.0,
            temperature=0.6,
            echo=True
        )
print("GPT3 Response: ", response)

def generate_prompt(keyword):
    return """Speculate on what the next update for Unreal Engine 5 will be"""

print(response.choices[0].text)
