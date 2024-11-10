import json
import os
from openai import OpenAI
client = OpenAI


class GPTHelper:
  def __init__(self):
    try:
      with open("config/openai_credentials.json") as f:
        data = json.load(f)
        self.client = OpenAI(api_key=data["api_key"])
        print("OpenAI client created")
    except FileNotFoundError:
      self.client = None
      raise FileNotFoundError("Error fetching OpenAI credentials. Please ensure that config/openai_credentials.json exists and is of correct format.")
    except json.JSONDecodeError:
      self.client = None
      raise json.JSONDecodeError("Error decoding OpenAI credentials. Please ensure that config/openai_credentials.json exists and is of correct format.")
    

async def generate_text(prompt, max_tokens=100):
   gpthelper = GPTHelper()
   completion = await gpthelper.client.chat.completions.create(
     model="gpt-4o-mini",
     messages=[
       {
         "role": "system",
         "content": "I just want to test stuff."
       }
     ]
   );
   print(completion)
   return completion


