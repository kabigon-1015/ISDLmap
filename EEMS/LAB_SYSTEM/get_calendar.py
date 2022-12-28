from __future__ import print_function
import datetime
import pickle
import os.path
import pprint
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import sort_schedule

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'C:/Users/hayat/Downloads/nyutaishitu/nyutaishitu/nyutaishitu/EEMS/LAB_SYSTEM/client_secret.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds, cache_discovery=False)

    # Call the Calendar API
    # at KC101
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    nowdate = datetime.datetime.strptime(now[:-8], '%Y-%m-%dT%H:%M:%S')
    recentdate = nowdate+datetime.timedelta(hours=1)
    recent = recentdate.strftime('%Y-%m-%dT%H:%M:%S') + 'Z'
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='mikilab.doshisha.ac.jp_3739313235333736353437@resource.calendar.google.com', timeMin=now,
                                        timeMax=recent, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    calendarId='mikilab.doshisha.ac.jp_3739313235333736353437@resource.calendar.google.com'

    g = []
    none = []
    count = 0
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        if checktime(start,nowdate,count):
            g.append(sort_schedule.sort_schedule_now(event,calendarId,count))
            count += 1
        else:
            count += 1
            g.append(none)
            g.append(sort_schedule.sort_schedule_now(event,calendarId,count))
            count += 1
    for i in range(2-count):
        g.append(none)

    # Call the Calendar API
    # at KC103
    events_result = service.events().list(calendarId='mikilab.doshisha.ac.jp_33353234353936362d333132@resource.calendar.google.com', timeMin=now,
                                        timeMax=recent, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    calendarId='mikilab.doshisha.ac.jp_33353234353936362d333132@resource.calendar.google.com'

    count = 0
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        if checktime(start,nowdate,count):
            g.append(sort_schedule.sort_schedule_now(event,calendarId,count))
            count += 1
        else:
            count += 1
            g.append(none)
            g.append(sort_schedule.sort_schedule_now(event,calendarId,count))
            count += 1
    for i in range(2-count):
        g.append(none)
    print(g)

    # Call the Calendar API
    # at KC111
    events_result = service.events().list(calendarId='mikilab.doshisha.ac.jp_3235333239333534343633@resource.calendar.google.com', timeMin=now,
                                        timeMax=recent, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    calendarId='mikilab.doshisha.ac.jp_3235333239333534343633@resource.calendar.google.com'

    count = 0
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start)
        if checktime111(start,nowdate,count):
            g.append(sort_schedule.sort_schedule_now(event,calendarId,count))
            count += 1
        else:
            count += 1
            g.append(none)
            g.append(sort_schedule.sort_schedule_now(event,calendarId,count))
            count += 1
    for i in range(2-count):
        g.append(none)
    print(g)

    # Call the Calendar API
    # at KC116
    events_result = service.events().list(calendarId='mikilab.doshisha.ac.jp_38363338373137302d343939@resource.calendar.google.com', timeMin=now,
                                        timeMax=recent, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    calendarId='mikilab.doshisha.ac.jp_38363338373137302d343939@resource.calendar.google.com'

    count = 0
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start)
        if checktime111(start,nowdate,count):
            g.append(sort_schedule.sort_schedule_now(event,calendarId,count))
            count += 1
        else:
            count += 1
            g.append(none)
            g.append(sort_schedule.sort_schedule_now(event,calendarId,count))
            count += 1
    for i in range(2-count):
        g.append(none)
    print(g)

    # Call the Calendar API
    # at KC119
    events_result = service.events().list(calendarId='mikilab.doshisha.ac.jp_38363935323038372d393739@resource.calendar.google.com', timeMin=now,
                                        timeMax=recent, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    calendarId='mikilab.doshisha.ac.jp_38363935323038372d393739@resource.calendar.google.com'

    count = 0
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start)
        if checktime111(start,nowdate,count):
            g.append(sort_schedule.sort_schedule_now(event,calendarId,count))
            count += 1
        else:
            count += 1
            g.append(none)
            g.append(sort_schedule.sort_schedule_now(event,calendarId,count))
            count += 1
    for i in range(2-count):
        g.append(none)
    print(g)

    return g

def checktime(start, nowdate, count):
    startdate = datetime.datetime.strptime(start[:-1], '%Y-%m-%dT%H:%M:%S')
    print(startdate,nowdate,count)
    if startdate < nowdate and count == 0:
        return True
    if startdate > nowdate and count == 1:
        return True
    return False

def checktime111(start,nowdate,count):
    startdate = datetime.datetime.strptime(start[:-6], '%Y-%m-%dT%H:%M:%S')
    print(startdate,nowdate,count)
    if startdate < nowdate and count == 0:
        return True
    if startdate > nowdate and count == 1:
        return True
    return False

if __name__ == '__main__':
    g = main()