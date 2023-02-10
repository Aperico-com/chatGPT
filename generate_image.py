import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key=os.getenv('OPENAI_API_KEY')

print("Calling GPT3")
st = time.time()
openai.Image.create(
  prompt="rural romantic lanscape impressionist aquarelle",
  n=1,
  size="1024x1024"
)
print("Response time: ", time.time() - st, "s")