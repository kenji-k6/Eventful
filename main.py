from datetime import datetime
import calendar
import json

if __name__ == "__main__":
  # test = GoogleServiceManager()
  # gmail_test_service = test.get_gmail_service()
  # test_messages = get_messages(service=gmail_test_service, query="is:starred from:kenji.y.nakano@gmail.com ")


  # test_message = gmail_test_service.users().messages().get(userId="me", id=test_messages[0]["id"]).execute()

  # test_reply_msg_id = test_message["id"]
  # print(test_message["snippet"])
  # assert(test_message["snippet"] == "Test 123 readme readme Test123")
  # create_reply_draft(service=gmail_test_service, message_id=test_reply_msg_id, draft_text="Hello, this is a test")

  # with open("config/test_email.json") as f:
  #   data = json.load(f)
  #   message = "Subject: " + data["subject"] + "\n\n" + "Content: " + data["content"]
  #   print(message)
  #   res = test_event_generate(message)
  #   print(res)
  temp = datetime(2024, 11, 18).date()
  print(calendar.day_name[temp.weekday()])
  print(str(temp))