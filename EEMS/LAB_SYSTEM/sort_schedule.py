from __future__ import print_function
import datetime
import pickle
import os.path
import pprint
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def sort_schedule_now(event, calendarId, count):
    schedules = []
    room = get_room(calendarId)
    start = event['start'].get('dateTime', event['start'].get('date'))
    end = event['end'].get('dateTime', event['end'].get('date'))
    if room == "KC111":
        start = datetime.datetime.strptime(start[:-6], '%Y-%m-%dT%H:%M:%S')
        end = datetime.datetime.strptime(end[:-6], '%Y-%m-%dT%H:%M:%S')
    elif room == "KC116" or room == "KC119":
        start = datetime.datetime.strptime(start[:-6], '%Y-%m-%dT%H:%M:%S')
        end = datetime.datetime.strptime(end[:-6], '%Y-%m-%dT%H:%M:%S')
    else:
        start = datetime.datetime.strptime(start[:-1], '%Y-%m-%dT%H:%M:%S')
        end = datetime.datetime.strptime(end[:-1], '%Y-%m-%dT%H:%M:%S')
    guest = event.get('attendees')
    summary = event['summary']

    message = generate_message(start,end,summary,room,count)

    #start = str(start.hour) + ":" + str(start.minute)
    schedules.append(message)
    for i in guest:
        dic = i
        schedules.append(dic.get('email'))
    schedules = [i for i in schedules if i != calendarId and i != 'mikilab.doshisha.ac.jp_38363935323038372d393739@resource.calendar.google.com']
    print(schedules)
    print("\n")
    return schedules

def hour_change(hour,room):
    if room == "KC111":
        new_hour = hour
    elif room == "KC116" or room == "KC119":
        new_hour = hour + 16
    else:
        new_hour = hour + 9
    if(new_hour >= 24):
        new_hour = new_hour % 24
    return new_hour

def get_room(id):
    if id == 'mikilab.doshisha.ac.jp_3739313235333736353437@resource.calendar.google.com':
        return "KC101"
    if id == 'mikilab.doshisha.ac.jp_33353234353936362d333132@resource.calendar.google.com':
        return "KC103"
    if id == 'mikilab.doshisha.ac.jp_3235333239333534343633@resource.calendar.google.com':
        return "KC111"
    if id == 'mikilab.doshisha.ac.jp_38363338373137302d343939@resource.calendar.google.com':
        return "KC116"
    if id == 'mikilab.doshisha.ac.jp_38363935323038372d393739@resource.calendar.google.com':
        return "KC119"
    return "room"

def generate_message(start, end, summary, room, count):
    message = ""
    if (count == 1):
        message += str(hour_change(start.hour,room)) + ":" + str(start.minute).rjust(2,'0') + "から" 
    message += str(hour_change(end.hour,room)) + ":" + str(end.minute).rjust(2,'0') + "まで<br>"
    message += summary + "で<br>"
    message += room + "を使う"
    if (count == 0):
        message += "よ！"
    else:
        message += "予定だよ！"
    return message