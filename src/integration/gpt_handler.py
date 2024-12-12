import json
from openai import OpenAI
from typing import Optional
from src.integration.extraction_schemas import MeetingEventSubjectDateTime, MeetingEventFixedOrProposal, MeetingEventLinkLocation
client = OpenAI

class MeetingEvent():
  subject: str
  start_date_time: list[str]
  end_date_time: list[str]

  is_proposal: bool

  is_virtual: list[Optional[bool]]
  location: list[Optional[str]]
  link: list[Optional[str]]

  def __init__(self, subject: str, start_date_time: list[str], end_date_time: list[str], is_proposal: list[Optional[bool]], is_virtual: list[Optional[bool]], location: list[Optional[str]], link: list[Optional[str]]):
    self.subject = subject
    self.start_date_time = start_date_time
    self.end_date_time = end_date_time
    self.is_proposal = is_proposal
    self.is_virtual = is_virtual
    self.location = location
    self.link = link
    


class GPTHelper:
  def __init__(self, default_duration="1H", default_morning="9:00", default_afternoon="14:00", default_evening="18:00"):
    try:
      with open("config/openai_credentials.json") as f:
        data = json.load(f)
        self.client = OpenAI(api_key=data["api_key"])
        self.model = "gpt-4o-mini"

        self.default_duration = default_duration
        self.default_morning = default_morning
        self.default_afternoon = default_afternoon
        self.default_evening = default_evening

        print("OpenAI client created")
    except FileNotFoundError:
      self.client = None
      raise FileNotFoundError("Error fetching OpenAI credentials. Please ensure that config/openai_credentials.json exists and is of correct format.")
    except json.JSONDecodeError:
      self.client = None
      raise json.JSONDecodeError("Error decoding OpenAI credentials. Please ensure that config/openai_credentials.json exists and is of correct format.")
  

  def get_event_subject_date_time(self, message) -> MeetingEventSubjectDateTime:
    q = f"Extract the subject, and date times individually for each meeting. There might be more than one meeting. Watch out for keywords like \"next week\". Default duration: {self.default_duration}. Default morning time: {self.default_morning}. Default afternoon time: {self.default_afternoon}. Default evening time: {self.default_evening} Date-Time format: YYYY-MM-DDTHH:MM:SS."

    completion = self.client.beta.chat.completions.parse(
      model=self.model,
      messages=[
        {"role": "system", "content": q},
        {"role": "user", "content": message},
      ],
      response_format=MeetingEventSubjectDateTime,
    )
    return completion.choices[0].message.parsed
  

  def get_event_fixed_or_proposal(self, message) -> MeetingEventFixedOrProposal:
    q = "Determine whether the meeting is a fixed scheduled meeting or a proposed meeting."

    completion = self.client.beta.chat.completions.parse(
      model=self.model,
      messages=[
        {"role": "system", "content": q},
        {"role": "user", "content": message},
      ],
      response_format=MeetingEventFixedOrProposal,
    )
    return completion.choices[0].message.parsed
  
  def get_event_link_location(self, message) -> MeetingEventLinkLocation:
    q = "For each proposed meeting time individually, determine whether the meeting is virtual, and the location or link. If some information is missing, use a null value."
    completion = self.client.beta.chat.completions.parse(
      model=self.model,
      messages=[
        {"role": "system", "content": q},
        {"role": "user", "content": message},
      ],
      response_format=MeetingEventLinkLocation,
    )
    return completion.choices[0].message.parsed


  def get_event_info(self, message) -> MeetingEvent:
    subject_date_time = self.get_event_subject_date_time(message)
    fixed_or_proposal = self.get_event_fixed_or_proposal(message)
    link_location = self.get_event_link_location(message)

    return MeetingEvent(subject=subject_date_time.subject,
                        start_date_time=subject_date_time.start_date_time,
                        end_date_time=subject_date_time.end_date_time,
                        is_proposal=fixed_or_proposal.is_proposal,
                        is_virtual=link_location.is_virtual,
                        location=link_location.location,
                        link=link_location.link,
                        )
  




