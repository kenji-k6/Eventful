import json
import os
from openai import OpenAI
from pydantic import BaseModel
from typing import Optional
client = OpenAI



class MeetingEvent(BaseModel):
  name: str

  start_date_time: list[str]

  meeting_time_is_proposal: bool

  end_date_time: list[str]
  meeting_is_virtual: list[bool]

  location_or_link: list[Optional[str]]



class GPTHelper:


  def __init__(self, default_meeting_duration="1H", dates_relative_to="today", default_morning="9:00", default_afternoon="13:00", default_evening="18:00"):
    try:
      with open("config/openai_credentials.json") as f:
        data = json.load(f)
        self.client = OpenAI(api_key=data["api_key"])
        self.QUERY = f"Extract the event details from the email. Ensure all lists are of equal length. Default meeting duration: {default_meeting_duration}. Default Morning Time: {default_morning}. Default Afternoon Time: {default_afternoon}. Default Evening Time: {default_evening}. Date-Time Format: YYYY-MM-DDTHH:MM:SS. Make the dates relative to: {dates_relative_to}"
        print("OpenAI client created")
    except FileNotFoundError:
      self.client = None
      raise FileNotFoundError("Error fetching OpenAI credentials. Please ensure that config/openai_credentials.json exists and is of correct format.")
    except json.JSONDecodeError:
      self.client = None
      raise json.JSONDecodeError("Error decoding OpenAI credentials. Please ensure that config/openai_credentials.json exists and is of correct format.")
    
  def get_event_info(self, message) -> MeetingEvent:
    completion = self.client.beta.chat.completions.parse(
      model="gpt-4o-mini",
      messages=[
        {"role": "system", "content": self.QUERY},
        {"role": "user", "content": message},
      ],
      response_format=MeetingEvent,
    )
    return completion.choices[0].message.parsed
  




