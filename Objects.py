class Event:
    def __init__(self, name, weekDays, time):
        self.name=name
        self.weekDays=weekDays
        self.time=time

    def frequencyPerWeek(self):
        return len(self.weekDays)

    def getName(self):
        return self.name

    def getWeekDays(self):
        return self.weekDays

    def getTime(self):
        return self.time

    def getCertainTimeOfDay(self, index):
        return self.time[index]

    def addFormalTime(self, x):
        self.datetimeTime=x
        return self

    def getFormalTime(self):
        return self.datetimeTime
