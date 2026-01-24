import time
import pandas as pd
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align


#=========================================Classes and Functions============================================
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

    return [round(hours), round(minutes), round(seconds)]

def generate_table():
    table = Table(title="Mining Collectables", title_style= "cyan", header_style= "cyan", expand=True, style="cyan")
    table.add_column("Name", justify='center')
    table.add_column("Level", justify='center')
    table.add_column("Time", justify='center')
    return table

def generate_panel(time):
    return Panel(Align.center(f"{time[0]}:{time[1]}:{time[2]}", vertical='middle'), title="Eorzean Time", style="red")


#===========================================Main Code==================================================

#creating layout
layout = Layout()
layout.split_column( 
    Layout(name="Eorzean Time"),
    Layout(name="Collectables")
)
layout["Eorzean Time"].size = 5



#retrieve information from csv
resourceTable = pd.read_csv(r"C:\repos\ffxivPersonalResourceTracker\resourceTable.csv")
resourceList = resourceTable.values.tolist()

#create item table
itemTable = []
for i in resourceList:
    itemTable.append(item(i[0], i[1], i[2], i[3]))


#generate initial renderables
console = Console()
table = generate_table()
panel = generate_panel(calculateTime())

#live updating
with Live(layout, refresh_per_second=1, screen=True) as live:
    while True:

        #constructing new renderables
        output = calculateTime()
        panel = generate_panel(output)
        table = generate_table()

        #calculate limited collectables that are available
        for i in itemTable:
            if i.timeStart <= output[0] and (i.timeEnd > output[0] or (i.timeEnd == 23 and output[0] == 23)):
                table.add_row(
                    Align.center(str(i.name), vertical='middle'), 
                    Align.center(str(i.level), vertical='middle'), 
                    Align.center(f"{i.timeStart}:00 - {i.timeEnd}:00", vertical='middle'),
                    style = "cyan"
                )

        #update panel and tables
        layout["Eorzean Time"].update(panel)
        layout["Collectables"].update(table)


    