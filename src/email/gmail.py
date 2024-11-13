import base64
from googleapiclient.errors import HttpError
from email.mime.text import MIMEText



def get_messages(service, query: str) -> list:
  """
  Fetches email messages from the user's inbox that match a specific query.

  Parameters:
  ----------
  query : str
      The search query to filter messages in the inbox (e.g., "in:unread").
  service : googleapiclient.discovery.Resource
      The authenticated Gmail API service instance.

  Returns:
  -------
  list
      A list of message metadata dictionaries that match the query. Each dictionary contains 
      details like 'id' and 'threadId'. Returns an empty list if no messages are found or 
      if an error occurs.

  Raises:
  ------
  HttpError
      If an error occurs while attempting to connect to the Gmail API.
  """

  try:
    
    results = service.users().messages().list(userId="me", labelIds=["INBOX"], q=query).execute()
    messages = results.get("messages", [])

    return messages

  except HttpError as error:
    print("An error occurred:", error)
    


def create_reply_draft(service, message_id, draft_text):

  try:
    # Retrieve original email to get headers
    message = service.users().messages().get(userId="me", id=message_id).execute()
    message_payload = message["payload"]
    headers = {header["name"]: header["value"] for header in message_payload["headers"]}


    # Get required headers to ensure draft is a reply, not a new message
    thread_id = message["threadId"]
    subject = headers.get("Subject", "No Subject")
    email_src = headers.get("From")



    print("Message thread ID:", thread_id)
    print("Message subject:", subject)


    # Create MIMEText object for draft
    mime_message = MIMEText(draft_text, "plain", "utf-8")
    mime_message["to"] = email_src
    mime_message["subject"] = f"Re: {subject}"
    mime_message["In-Reply-To"] = message_id
    mime_message["References"] = message_id

    # Encode MIMEText object to base64
    encoded_message = base64.urlsafe_b64encode(mime_message.as_bytes()).decode("utf-8")

    # Create draft message
    draft_body = {
      "message": {
        "raw": encoded_message,
        "threadId": thread_id
      }
    }
    draft = service.users().drafts().create(userId="me", body=draft_body).execute()
    print("Draft created for:", email_src)
    return draft
  

  except HttpError as error:
    print("An error occurred:", error)
