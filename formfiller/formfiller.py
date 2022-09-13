from data import timetable, weekdays, entries
import webbrowser
import keyboard
import os
from datetime import datetime, time, timedelta
from time import sleep
from dotenv import load_dotenv
load_dotenv()

NAME = os.getenv("NAME")
SURNAME = os.getenv("SURNAME")
FORM = os.getenv("FORM") + "formResponse?"

today = datetime.now()
periodtimes = [
    datetime.combine(today, time(8, 55, 0)),
    datetime.combine(today, time(9, 40, 0)),
    datetime.combine(today, time(10, 40, 0)),
    datetime.combine(today, time(11, 20, 0)),
    datetime.combine(today, time(12, 45, 0)),
    datetime.combine(today, time(13, 30, 0))
]


def finalform(period):
    week = "Week+B"  # to be manually changed every week
    weekday = weekdays[today.weekday()]
    year = str(today.year)
    month = str(today.month)
    month = "0" + month if len(month) == 1 else month
    day = str(today.day)
    day = "0" + day if len(day) == 1 else day
    bigform = FORM
    bigform += entries["name"] + "=" + NAME + "&"
    bigform += entries["surname"] + "=" + SURNAME + "&"
    bigform += entries["year"] + "=" + year + "&"
    bigform += entries["month"] + "=" + month + "&"
    bigform += entries['day'] + '=' + day + "&"
    bigform += entries["week"] + "=" + week + "&"
    bigform += entries["weekday"] + '=' + weekday + "&"
    bigform += entries["periodb"][today.weekday()] + '=' + str(period) + "&"
    bigform += timetable[today.weekday()][period - 1][1] + \
        "=" + timetable[today.weekday()][period - 1][0]
    return bigform


def submit(period):
    webbrowser.open(finalform(period))
    sleep(2)
    keyboard.send("tab")
    keyboard.send("tab")
    keyboard.send("enter")
    sleep(1)
    keyboard.press("ctrl")
    keyboard.send("w")
    keyboard.release("ctrl")


submit(1)

for i in range(6 if today.weekday() != 2 else 3):
    submit(i + 1)
    sleep((periodtimes[i] - datetime.now()).total_seconds())
