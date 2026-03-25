from datetime import date, timedelta, datetime, time
from time import sleep
from plyer import notification
from Objects import Event
from requests import get
from math import ceil
import json
from tkinter import

def sleepUntilTomorrow():
    presentDay = date.today()
    tomorrowDay = presentDay + timedelta(days=1)
    datetimeTomorrow = datetime.combine(tomorrowDay, time.min)
    TimeTillTomorrow = datetimeTomorrow - datetime.now()
    sleep(TimeTillTomorrow.total_seconds())

def notificate(title, message, app_name):
    notification.notify(title, message, app_name)

def sortedEventsToday(dayParameters, events):
    eventsToday=[]
    for i in events:
        if dayParameters[-1] in i.weekDays:
            if len(i.time)==1:
                timeOfEvent=i.time[0]
            else:
                timeOfEvent=i.time[i.weekDays.index(dayParameters[-1])]
            currEvent=Event(i.getName(), dayParameters[-1], timeOfEvent)
            j_day = f"{dayParameters[0]}, {dayParameters[1]}, {dayParameters[2]}, {currEvent.time}"
            eventsToday.append(currEvent.addFormalTime(datetime.strptime(j_day, "%B, %d, %Y, %X")))
    return sorted(eventsToday, key=lambda x: x.getFormalTime())

def iterateEvents(eventsToday):
    for i in range(len(eventsToday)):
        deltaTime = eventsToday[i].getFormalTime()-datetime.today()
        if deltaTime.total_seconds() > 60*2*60:
            sleep(deltaTime.total_seconds()-60*2*60)
            notificate(f"{eventsToday[i].getName()} today","Two hours left","Reminder")
            deltaTime=deltaTime-timedelta(seconds=deltaTime.total_seconds()-60*2*60)
        elif 60*60 < deltaTime.total_seconds() < 60*60*2:
            notificate(f"{eventsToday[i].getName()} soon", "Get ready", "Reminder")
            sleep(deltaTime.total_seconds()-60*60)
            deltaTime=deltaTime-timedelta(seconds=deltaTime.total_seconds()-60*60)
        if deltaTime.total_seconds() > 60*60:
            sleep(60*60)
            deltaTime = deltaTime - timedelta(seconds=60 * 60)
        else:
            sleep(deltaTime.total_seconds()-30*60)
            deltaTime=deltaTime-timedelta(seconds=deltaTime.total_seconds()-30*60)

        notificate(f"{eventsToday[i].getName()}", "Final reminder", "Reminder")

        sleep(deltaTime.total_seconds())

def courseExistence(courseNameEn):
    base_url = "https://api.srv.nat.tum.de"

    params = {"semester_key": "next", "order_by": "code", "offset": "0", "limit": "200"}
    numOfCourses = get(base_url + "/api/v1/course", params=params).json()["total_count"]

    wasFound = False

    upperBound = ceil(numOfCourses / 200) * 200
    while (int(params["offset"]) != upperBound):
        res = get(base_url + "/api/v1/course", params=params).json()["hits"]
        for i in res:
            if i["course_name_secondary"] == courseNameEn:
                wasFound = True
                break
        if wasFound:
            break
        params["offset"] = str(int(params["offset"]) + 200)

    return wasFound


def createEvents(num, events):
    if num > 0:
        while num > 0:
            name = input("Enter the name of the event: ")
            weekDays = input("Enter the days the event takes place on: ")
            time = input("Enter the times the event takes place at: ")
            if " " in weekDays:
                weekDays=weekDays.split(" ")
            else:
                tempDaysList=[]
                tempDaysList.append(weekDays)
            if " " in time:
                time = time.split(" ")
            else:
                tempTimeList=[]
                tempTimeList.append(time)
            events.append(Event(name, tempDaysList, tempTimeList))
            num-=1
        with open("Remembrance.json", "w") as file:
            info=[]
            for i in events:
                currElement={"name": f"{i.getName()}", "weekDays": f"{i.weekDays()}", "time": f"{i.getTime()}"}
                info.append(currElement)
            json.dump(info, file, ensure_ascii=False, indent=2)

def input_check(string):
    return True if string.isdigit() else False

def open_file_dialog():


# def addEventsFromCalender(path):
