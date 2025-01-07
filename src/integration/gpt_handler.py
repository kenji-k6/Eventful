import json
import os
from openai import OpenAI
from pydantic import BaseModel
from typing import Optional
client = OpenAI


class MeetingEvent(BaseModel):
  name: str
  start_time: str
  end_time: Optional[str]
  description: Optional[str]
  participants: list[str]
  location: Optional[str]
  meeting_link: Optional[str]
  meeting_is_virtual: bool 
  meeting_time_is_proposal: bool



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




# async def generate_text(prompt, max_tokens=100):
#    gpthelper = GPTHelper()
#    completion = await gpthelper.client.chat.completions.create(
#      model="gpt-4o-mini",
#      messages=[
#        {
#          "role": "system",
#          "content": "I just want to test stuff."
#        }
#      ]
#    );
#    print(completion)
#    return completion

def test_event_generate(message):
  gpthelper = GPTHelper()
  completion = gpthelper.client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": "Extract the event details from the email."},
      {"role": "user", "content": message},
    ],
    response_format=MeetingEvent,
  )

  temp = completion.choices[0].message.parsed
  print(temp)



