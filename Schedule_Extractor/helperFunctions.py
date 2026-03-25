from ordered_set import OrderedSet
import json

geToEn = {"MO": "Monday", "DI": "Tuesday", "MI": "Wednesday", "DO": "Thursday", "FR": "Friday"}

def orderedsetToList(dictrionary):
    for key, value in dictrionary.items():
        newWeekdaysList=[]
        for i in value[0]:
            newWeekdaysList.append(i)
        dictrionary[key][0]=newWeekdaysList

def removeDuplicates(dictionary):
    for key, value in dictionary.items():
        if len(value[0])<len(value[1]):
            newTimeList=[]
            if len(value[0])%2==0:
                for i in range (0, len(value[1]), 2):
                    newTimeList.append(value[1][i])
            else:
                for i in range (1, len(value[1]), 2):
                    newTimeList.append(value[1][i])

            dictionary[key][1]=newTimeList

def parseData(root):
    res={}
    for row in root:
        title = row.find("TITEL").text
        beginTime = row.find("VON").text + ":00"
        weekDay = geToEn[row.find("WOCHENTAG").text]
        if title in res.keys():
            res[title][0].append(weekDay)
            res[title][1].append(beginTime)
        else:
            dayToAdd = OrderedSet()
            dayToAdd.append(weekDay)
            res[title] = [dayToAdd, [beginTime]]

    return res

def updateJSON(info):
    with open("../Remembrance.json", "r+") as file:
        initial_info = json.load(file)
        for key, value in info.items():
            initial_info.append({"name": key, "weekDays": value[0], "time": value[1]})
        json.dump(initial_info, file, ensure_ascii=False, indent=2)