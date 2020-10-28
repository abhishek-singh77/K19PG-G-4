import pandas as pd
from tkinter import *
import os

# GUI display for live parking slots
def disp():
    global rl
    global cl

    # inserting csv file for live checking live parking positions available

    df = pd.read_csv('Data' + os.path.sep + "map_grid.csv", header=None)
    rl = df.shape[1]  # total row count
    cl = df.shape[0]  # total column count
    df.dropna(axis=0)
    temp = df.values.tolist()
    root1 = Tk()  # build GUI
    root1.title("Live Parking Slots")
    root1.geometry("600x700")
    frame = Frame(root1)
    Grid.rowconfigure(root1, 0, weight=1)
    Grid.columnconfigure(root1, 0, weight=1)
    frame.grid(row=0, column=0, sticky=N + S + E + W)
    grid = Frame(frame)
    grid.grid(sticky=N + S + E + W, column=0, row=rl + 1, columnspan=2)
    Grid.rowconfigure(frame, rl, weight=1)
    Grid.columnconfigure(frame, 0, weight=1)

    # ma= Matrix for parking slot
    # T=Taken
    # S=Start
    # E=Empty
    # P=Path
    # Sample format
    '''CSV format:-
    temp=[
    ['S','P','P','P','E'],
    ['P','T','T','P','E'],
    ['P','E','E','P','E'],
    ['P','T','T','P','E'],
    ['P','P','P','P','E'],
    ['E','E','E','E','E']
    ]'''

    emp_count = 0
    filled_count = 0
    for x in range(cl):
        for y in range(rl):
            if (temp[x][y] == "P"):
                btn = Button(frame, bg="grey")
                btn.grid(column=x, row=y, sticky=N + S + E + W)
            if (temp[x][y] == "E"):
                btn = Button(frame, bg="yellow")
                btn.grid(column=x, row=y, sticky=N + S + E + W)
                emp_count += 1
            if (temp[x][y] == "S"):
                btn = Button(frame, bg="blue", )
                btn.grid(column=x, row=y, sticky=N + S + E + W)
            if (temp[x][y] == "T"):
                btn = Button(frame, bg="red")
                btn.grid(column=x, row=y, sticky=N + S + E + W)
                filled_count += 1

    for x in range(cl):
        Grid.columnconfigure(frame, x, weight=6)

    for y in range(rl):
        Grid.rowconfigure(frame, y, weight=5)

    root1.mainloop()


def shut():
    root1.destroy()
