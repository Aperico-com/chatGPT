import os
import time
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key=os.getenv('OPENAI_API_KEY')

print("Calling GPT3")
st = time.time()
response = openai.Edit.create(
  model="text-davinci-edit-001",
  input="A transformer model is a neural network that learns context and thus meaning by tracking relationships in sequential data like the words in this sentence. Transformer models apply an evolving set of mathematical techniques, called attention or self-attention, to detect subtle ways even distant data elements in a series influence and depend on each other. First described in a 2017 paper from Google, transformers are among the newest and one of the most powerful classes of models invented to date. They’re driving a wave of advances in machine learning some have dubbed transformer AI. Stanford researchers called transformers foundation models in an August 2021 paper because they see them driving a paradigm shift in AI. The sheer scale and scope of foundation models over the last few years have stretched our imagination of what is possible",
  instruction="Expand on this topic using scientific regression."
)
print("Response time: ", time.time() - st, "s")

print(response.choices[0].text)