from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

SCOPES = ["https://www.googleapis.com/auth/calendar"]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.path.join(BASE_DIR, "../config/credentials.json")
TOKEN_FILE = os.path.join(BASE_DIR, "../data/token.pickle")


def authenticate_google_calendar():
    creds = None
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"ERROR: Missing credentials file: {CREDENTIALS_FILE}")
        print(
            "Make sure you have a valid Google API credentials.json in the /config/ folder."
        )
        return None

    if os.path.exists(TOKEN_FILE):
        try:
            with open(TOKEN_FILE, "rb") as token:
                creds = pickle.load(token)
        except (EOFError, pickle.UnpicklingError):
            print(
                "Corrupted token.pickle file detected. Deleting and re-authenticating."
            )
            os.remove(TOKEN_FILE)
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"Token refresh failed: {e}")
                creds = None
        if not creds:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        os.makedirs(os.path.dirname(TOKEN_FILE), exist_ok=True)
        with open(TOKEN_FILE, "wb") as token:
            pickle.dump(creds, token)

    return creds
