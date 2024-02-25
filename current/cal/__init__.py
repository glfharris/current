import os
from gcsa.google_calendar import GoogleCalendar
from google.oauth2.credentials import Credentials

CURRENT_CAL_ID = "3a784af39e091f5fb78f38e1f205f562548f7cba1819c5a4c2c0ef7c10194e4b@group.calendar.google.com"

token = Credentials(
        token=os.getenv("G_TOKEN"),
        refresh_token=os.getenv("G_REFRESH_TOKEN"),
        client_id=os.getenv("G_CLIENT_ID"),
        client_secret=os.getenv("G_CLIENT_SECRET"),
        scopes=["https://www.googleapis.com/auth/calendar"],
        token_uri="https://oauth2.googleapis.com/token"
)

calendar = GoogleCalendar(CURRENT_CAL_ID, credentials=token)
