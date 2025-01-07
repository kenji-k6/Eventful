from src.auth.auth import GoogleServiceManager
from src.email_processing.gmail import get_messages

if __name__ == "__main__":
  test = GoogleServiceManager()
  gmail_test_service = test.get_gmail_service()
  test_messages = get_messages(query="in:unread", service=gmail_test_service)

  for message in test_messages:
    msg = gmail_test_service.users().messages().get(userId="me", id=message["id"]).execute()
    print(msg["snippet"])