import time
import pandas



class item:
    def __init__(self, name, level, timeStart, timeEnd):
        self.name = name
        self.level = level
        self.timeStart = timeStart
        self.timeEnd = timeEnd

def calculateTime():
    realTime = time.time()
    gameTime = realTime * 20.57142857142857
    
    hours = gameTime//3600 % 24
    minutes = gameTime // 60 % 60
    seconds = gameTime % 60

    print(f"{round(hours)}:{round(minutes)}:{seconds:.2f}")

    return hours


itemTable = [
    item("Rarefield Pyrite", 51, 4, 6),
    item("Rarefield Pyrite", 51, 16, 18),
    item("Rarefield Cholcocite", 53, 4, 6),
    item("Rarefield Cholcocite", 53, 16, 18),
    item("Rarefield Limonite", 53, 4, 6),
    item("Rarefield Limonite", 53, 16, 18),
    item("Rarefield Abalathian Spring Water", 57, 2, 4),
    item("Rarefield Abalathian Spring Water", 57, 14, 16),
    item("Rarefield Aurum Regis Sand", 59, 2, 4),
    item("Rarefield Aurum Regis Sand", 59, 14, 16),
    item("Rarefield Raw Triphane", 61, 8, 10),
    item("Rarefield Raw Triphane", 61, 20, 22),
    item("Rarefield Raw Star Spinel", 63, 10, 12),
    item("Rarefield Raw Star Spinel", 63, 22, 23),
]
while(True):
    output = calculateTime()
    print()
    print("Gatherable Unspoiled Nodes:")
    for i in itemTable:
        if i.timeStart <= output and (i.timeEnd > output or (i.timeEnd == 23 and output == 23)):
            print(f"Name: {i.name}, Level: {i.level}, Time: {i.timeStart}:00 - {i.timeEnd}:00")


    time.sleep(5)
    print("\033[2J\033[H", end="")

    