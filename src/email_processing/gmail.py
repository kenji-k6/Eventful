from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from src.auth.auth import authenticate

creds = authenticate()
service = build("gmail", "v1", credentials=creds)



def list_unread_emails():
  try:
    
    results = service.users().messages().list(userId="me", labelIds=["INBOX"], q="from:invitations@linkedin.com").execute()
    messages = results.get("messages", [])

    print(len(messages))

    for message in messages:
      msg = service.users().messages().get(userId="me", id=message["id"]).execute()
      print(msg["snippet"])
  except HttpError as error:
    print("An error occurred:", error)
    


def gmail_test():
  list_unread_emails()
