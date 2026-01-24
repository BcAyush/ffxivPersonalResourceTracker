import time
import pandas as pd


#item object
class item:
    def __init__(self, name, level, timeStart, timeEnd):
        self.name = name
        self.level = level
        self.timeStart = timeStart
        self.timeEnd = timeEnd

#calculate in-game time
def calculateTime():
    realTime = time.time()
    gameTime = realTime * 20.57142857142857
    
    hours = gameTime//3600 % 24
    minutes = gameTime // 60 % 60
    seconds = gameTime % 60

    print(f"{round(hours)}:{round(minutes)}:{seconds:.2f}")

    return hours


itemTable = []

#retrieve information from csv
resourceTable = pd.read_csv(r"C:\repos\ffxivPersonalResourceTracker\resourceTable.csv")
resourceList = resourceTable.values.tolist()

#create item table
for i in resourceList:
    itemTable.append(item(i[0], i[1], i[2], i[3]))
    

#main code
while(True):
    output = calculateTime()
    print()
    print("Gatherable Unspoiled Nodes:")
    for i in itemTable:
        if i.timeStart <= output and (i.timeEnd > output or (i.timeEnd == 23 and output == 23)):
            print(f"Name: {i.name}, Level: {i.level}, Time: {i.timeStart}:00 - {i.timeEnd}:00")


    time.sleep(5)
    print("\033[2J\033[H", end="")

    