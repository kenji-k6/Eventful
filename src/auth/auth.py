from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

SCOPES = ["https://mail.google.com/"] #add scopes for meets abnd calendar


class GoogleServiceManager:
  def __init__(self):
    self.creds = None
    self.gmail_service = None
    self.calendar_service = None
    self.meet_service = None
  
  def get_gmail_service(self):
    if not self.gmail_service:
      creds = authenticate()
      self.gmail_service = build("gmail", "v1", credentials=creds)
    return self.gmail_service

  def get_calendar_service(self):
    print("TODO: Implement get_calendar_service()")

  def get_meet_service(self):
    print("TODO: Implement get_meet_service()")      




def authenticate():
  creds = None
  credentials_path = "config/user_credentials.json"

  # Check if config.json exists and load credentials
  if os.path.exists(credentials_path):
    creds = Credentials.from_authorized_user_file(credentials_path)

  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "config/credentials.json", SCOPES)
      creds = flow.run_local_server(port=0)

      # Save the credentials for the next run
      # This is done to avoid the user having to authenticate every time
      # the program is run
      # This is not recommended for production
      # For production, use a service account

      with open(credentials_path, 'w') as credentials_file:
        credentials_file.write(creds.to_json())

  return creds 
  

