from googleapiclient.errors import HttpError


def get_messages(query: str, service) -> list:
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
    
