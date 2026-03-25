# добавить память с json, тесты, команды чтобы через терминал работало

from Objects import Event
from datetime import datetime
import helperFunctinos
from tkinter import filedialog

events=[]
tags = {index: value for index, value in enumerate(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], 1)}

events_input = input("Put in the number of events: ")
while not helperFunctinos.input_check(events_input):
    events_input = input("Wrong input. Enter a number: ")
helperFunctinos.createEvents(events_input, events)

if input("Would u like to past an xml calender?").lower() == "yes":
    path
    helperFunctinos.addEventsFromCalender(input("Write the path to a file"))


try:

    tday = datetime.today()
    tday_time = tday.time()
    tday_date = tday.strftime("%B, %d, %Y, %X")

    mdyT = tday_date.split(", ")
    mdyT.append(tags[tday.isoweekday()])

    eventsToday=helperFunctinos.sortedEventsToday(mdyT, events)

    helperFunctinos.iterateEvents(eventsToday)

    helperFunctinos.sleepUntilTomorrow()

except KeyboardInterrupt:
    helperFunctinos.notificate("Interruption", "Programm stoppeed", "Reminder")
