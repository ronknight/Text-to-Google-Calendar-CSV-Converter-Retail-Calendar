import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import datetime

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def create_event(service, date, summary):
    event = {
      'summary': summary,
      'start': {
        'dateTime': date.isoformat(),
        'timeZone': 'America/New_York',
      },
      'end': {
        'dateTime': (date + datetime.timedelta(hours=1)).isoformat(),
        'timeZone': 'America/New_York',
      },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created:', event.get('htmlLink'))

def main():
    creds = authenticate()
    service = build('calendar', 'v3', credentials=creds)
    
    # Read data from the txt file
    with open('events.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            date_str, event_name = line.strip().split(',')
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            create_event(service, date, event_name)

if __name__ == '__main__':
    main()
