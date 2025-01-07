import json
from src.integration.gpt_handler import GPTHelper, MeetingEvent

# Date used to ensure tests are run on the same day
TEST_DATE = "2024-11-18"
TEST_DEFAULT_DURATION = "1H"
emails = []


# Test GPTHelper
gpt = GPTHelper(dates_relative_to=TEST_DATE)


# Auxiliary Debug functions
def print_dicts(meeting: dict, expect: dict) -> None:
  print("\n\n Extracted: \n")
  for key in expect:
    print(f"{key}:\n \t Extracted: {meeting[key]} \n\t Expected:  {expect[key]}")
    print("\n\n")





# Load test emails
try:
  with open("tests/test_emails.json") as f:
    emails = json.load(f)
except FileNotFoundError:
  print("Failed to load test emails. Please ensure that tests/test_emails.json exists and is of correct format.")
  raise FileNotFoundError("Error fetching test_emails.json. Please ensure that tests/test_emails.json exists and is of correct format.")


# Helper function to get message string
def get_message_str(stored_message) -> str:
  return "Subject: " + stored_message["subject"] + "\n\n" + "Content: " + stored_message["content"]


# Length assertions only for extracted dict
def extracted_length_assertions(meeting: dict) -> None:
  n = len(meeting["start_date_time"])

  # Make sure all length coincide
  assert(n == len(meeting["location_or_link"]))
  assert(n == len(meeting["end_date_time"]))
  assert(n == len(meeting["meeting_is_virtual"]))

  # if meeting is not just a proposal, make sure length is 1
  if not meeting["meeting_time_is_proposal"]:
    assert(n == 1)





def lengths_match_assertions(meeting: dict, expected: dict) -> None:
  assert(len(meeting["start_date_time"]) == len(expected["start_date_time"]))


def field_assertions(meeting: dict, expected: dict) -> None:
  for key in expected:
    if key == "name": continue
    if key == "meeting_time_is_proposal":
      if meeting[key] != expected[key]:
        print(f"Mismatch in {key}:\n")
        print_dicts(meeting, expected)
        assert(False)
      continue

    for i in range(len(expected[key])):
      if not expected[key][i] in meeting[key]:
        print(f"Mismatch in {key}:\n")
        print_dicts(meeting, expected)
        assert(False)




  
# Test functions
def test_get_event_info_0() -> None:
  message = get_message_str(emails[0])
  meeting = gpt.get_event_info(message).__dict__
  expected = emails[0]["result"]



  extracted_length_assertions(meeting)
  lengths_match_assertions(meeting, expected)
  field_assertions(meeting, expected)
  assert(True)
  

def test_get_event_info_1() -> None:
  message = get_message_str(emails[1])
  meeting = gpt.get_event_info(message).__dict__
  expected = emails[1]["result"]

  extracted_length_assertions(meeting)
  lengths_match_assertions(meeting, expected)
  field_assertions(meeting, expected)
  assert(True)


def test_get_event_info_2() -> None:
  message = get_message_str(emails[2])
  meeting = gpt.get_event_info(message).__dict__
  expected = emails[2]["result"]

  extracted_length_assertions(meeting)
  lengths_match_assertions(meeting, expected)
  field_assertions(meeting, expected)
  assert(True)


def test_get_event_info_3() -> None:
  message = get_message_str(emails[3])
  meeting = gpt.get_event_info(message).__dict__
  expected = emails[3]["result"]

  extracted_length_assertions(meeting)
  lengths_match_assertions(meeting, expected)
  field_assertions(meeting, expected)
  assert(True)


def test_get_event_info_4() -> None:
  message = get_message_str(emails[4])
  meeting = gpt.get_event_info(message).__dict__
  expected = emails[4]["result"]

  extracted_length_assertions(meeting)
  lengths_match_assertions(meeting, expected)
  field_assertions(meeting, expected)
  assert(True)


def test_get_event_info_5() -> None:
  message = get_message_str(emails[5])
  meeting = gpt.get_event_info(message).__dict__
  expected = emails[5]["result"]

  extracted_length_assertions(meeting)
  lengths_match_assertions(meeting, expected)
  field_assertions(meeting, expected)
  assert(True)


def test_get_event_info_6() -> None:
  message = get_message_str(emails[6])
  meeting = gpt.get_event_info(message).__dict__
  expected = emails[6]["result"]

  extracted_length_assertions(meeting)
  lengths_match_assertions(meeting, expected)
  field_assertions(meeting, expected)
  assert(True)


def test_get_event_info_7() -> None:
  message = get_message_str(emails[7])
  meeting = gpt.get_event_info(message).__dict__
  expected = emails[7]["result"]

  extracted_length_assertions(meeting)
  lengths_match_assertions(meeting, expected)
  field_assertions(meeting, expected)
  assert(True)


def test_get_event_info_8() -> None:
  message = get_message_str(emails[8])
  meeting = gpt.get_event_info(message).__dict__
  expected = emails[8]["result"]

  extracted_length_assertions(meeting)
  lengths_match_assertions(meeting, expected)
  field_assertions(meeting, expected)
  assert(True)


def test_get_event_info_9() -> None:
  message = get_message_str(emails[9])
  meeting = gpt.get_event_info(message).__dict__
  expected = emails[9]["result"]

  extracted_length_assertions(meeting)
  lengths_match_assertions(meeting, expected)
  field_assertions(meeting, expected)
  assert(True)


def test_get_event_info_10() -> None:
  message = get_message_str(emails[10])
  meeting = gpt.get_event_info(message).__dict__
  expected = emails[10]["result"]

  extracted_length_assertions(meeting)
  lengths_match_assertions(meeting, expected)
  field_assertions(meeting, expected)
  assert(True)


def test_get_event_info_11() -> None:
  message = get_message_str(emails[11])
  meeting = gpt.get_event_info(message).__dict__
  expected = emails[11]["result"]

  extracted_length_assertions(meeting)
  lengths_match_assertions(meeting, expected)
  field_assertions(meeting, expected)
  assert(True)