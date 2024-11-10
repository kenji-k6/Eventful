from src.auth.auth import GoogleServiceManager
from src.email_processing.gmail import get_messages, create_reply_draft
from src.email_processing.gpt_handler import GPTHelper, generate_text
import asyncio

if __name__ == "__main__":
  test = GoogleServiceManager()
  gmail_test_service = test.get_gmail_service()
  test_messages = get_messages(service=gmail_test_service, query="is:starred from:kenji.y.nakano@gmail.com ")


  test_message = gmail_test_service.users().messages().get(userId="me", id=test_messages[0]["id"]).execute()

  test_reply_msg_id = test_message["id"]
  print(test_message["snippet"])
  assert(test_message["snippet"] == "Test 123 readme readme Test123")
  # create_reply_draft(service=gmail_test_service, message_id=test_reply_msg_id, draft_text="Hello, this is a test")
  print(asyncio.run(generate_text("test")))