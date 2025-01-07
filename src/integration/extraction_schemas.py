from pydantic import BaseModel
from typing import Optional


class MeetingEventSubjectDateTime(BaseModel):
  subject: str

  start_date_time: list[str]
  end_date_time: list[str]


class MeetingEventFixedOrProposal(BaseModel):
  is_proposal: bool


class MeetingEventLinkLocation(BaseModel):
  is_virtual: list[Optional[bool]]
  location: list[Optional[str]]
  link: list[Optional[str]]
