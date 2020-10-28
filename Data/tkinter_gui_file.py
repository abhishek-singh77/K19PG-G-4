from Data.location_file import *
from Data.Map_file import *
from tkinter import *
from tkinter import messagebox
import sqlite3
import os
import datetime
import pandas as pd

toll = 54

# Main interface for parking
# building GUI
def main():
    global root
    root = Tk()
    root.title("AIA Parking Manager")
    global mobi
    global vehicle
    mobi = IntVar()
    vehicle = StringVar()
    root.iconbitmap(r'Data' + os.path.sep + 'logo.ico')
    canvas = Canvas(root, height=600, width=700, bg="#8B8BFB")
    canvas.pack()

    frame = Frame(root, bg="#8B8BFB")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(root, text="AIA Parking Management System", width=30, fg="black", bg="light blue",
                    font=("Park Lane", 22, "bold"))
    heading.place(x=75, y=18)
    total1 = Label(root, text="TOTAL", padx=62, pady=20, fg="white", font=(20), bg="#646F9A")
    total1.place(x=150, y=100)
    total2 = Label(root, text=toll, padx=60, pady=20, fg="white", font=(20), bg="#19191c")
    total2.place(x=330, y=100)

    avl1 = Label(root, text="AVAILABLE", padx=41, pady=20, fg="white", font=(20), bg="#585DC8")
    avl1.place(x=150, y=170)
    avl2 = Label(root, text=toll - addDB(), padx=60, pady=20, fg="white", font=(20), bg="#263D42")
    avl2.place(x=330, y=170)

    # NAME
    info1 = Label(root, text="Enter the Vehicle Number", width=20, fg="white", bg="#696c70", font=("bold", 19))
    info1.place(x=120, y=250)  # Display text
    entry1 = Entry(root, textvar=vehicle)
    entry1.place(x=450, y=250, height=40)

    # CONTACT NUMBER
    info2 = Label(root, text="Enter the Contact Number", width=20, fg="white", bg="#696c70", font=("bold", 19))
    info2.place(x=120, y=300)  # Display text
    entry2 = Entry(root, textvar=mobi)
    entry2.place(x=450, y=300, height=40)  # Enter contact

    # Park Button
    add = Button(root, text="PARK IN ", padx=5, pady=20, fg="orange", bg="yellow2", font=('Helvetica', 15, 'bold'), command=database)
    add.place(x=150, y=350)

    # Find location Button
    find = Button(root, text="FIND VEHICLE", padx=1, pady=20, fg="white", bg="yellow2", font=('Helvetica', 15, 'bold'), command=findLoc)
    find.place(x=275, y=350)

    # Remove Vehicle Button
    find = Button(root, text="PARK OUT", padx=1, pady=20, fg="green", bg="yellow2", font=('Helvetica', 15, 'bold'), command=deleteDB)
    find.place(x=450, y=350)
    # close
    close = Button(root, text="DONE", padx=15, pady=7, fg="black", bg="#E6EBF3", font=(17), command=action)
    close.place(x=300, y=547)

    root.resizable(0, 0)  # lock maximize option
    root.mainloop()






# database file
# create connection to database
def startDB():
    try:
        conn = sqlite3.connect('Data' + os.path.sep + 'location.db')
        return conn
    except Exception as e:
        print(e)
        return conn


# update location on map for filling
def loci():
    try:
        global rl, cl, toll, emp_count
        s, a, b, rl1, cl1 = position()
        # print(temp[1][4])
        rl = rl1
        cl = cl1
        df = pd.read_csv('Data' + os.path.sep + "map_grid.csv", header=None)
        df.dropna(axis=0)
        temp = df.values.tolist()
        temp[a][b] = 'T'
        pd.DataFrame(temp).to_csv('Data' + os.path.sep + "map_grid.csv", header=None, index=False)
        for i in temp:
            print(i)
        print("*******EOL******")


    except Exception as e:
        print(e, "OOPS!!! No more space available")
        msg = messagebox.showinfo(e, "OOPS!!! No more space available")


# create database

conn = startDB()
cursor = conn.cursor()

cursor.execute(
    'CREATE TABLE IF NOT EXISTS Location (Vehicle TEXT NOT NULL UNIQUE, Contact INT NOT NULL UNIQUE, Location_X INT, Location_Y INT,Date TEXT NOT NULL, Time TEXT NOT NULL)')
conn.commit()
cursor.close()


# add elements in database
def database():
    try:
        s, a, b, rl1, cl1 = position()
    except Exception as e:
        s = 0
        a = 0
        b = 0
        msg = messagebox.showinfo("Error!!!", "No more empty slots")
    now = datetime.datetime.now()
    Time = now.strftime("%H:%M:%S")
    Date = now.strftime("%d-%m-%Y")
    name = vehicle.get()
    try:
        mob = mobi.get()

    except Exception as e:
        msg2 = messagebox.showinfo("Error!!!", "Please Enter a valid Number")
        mob = 0

    posx = a  # x-axis of Location
    posy = b  # y-axis of location
    try:
        conn = startDB()
        cursor = conn.cursor()
        # cursor.execute('CREATE TABLE IF NOT EXISTS Location (Vehicle TEXT NOT NULL, Contact INT NOT NULL, Location INT NOT NULL, Date TEXT NOT NULL, Time TEXT NOT NULL)')
        cursor.execute(
            'INSERT INTO Location (Vehicle, Contact, Location_X, Location_Y, Date, Time) VALUES(?,?,?,?,?,?)',
            (name, mob, posx, posy, Date, Time))
        conn.commit()
        cursor.close()
        msg = messagebox.showinfo("Park Vehicle", "Park your Vehicle at (%d,%d)" % (posx, posy))
        park()
    except Exception as error:
        msg = messagebox.showinfo("Duplicate Error", "Please Enter Unique Elements")
    finally:
        if (conn):
            conn.close()


# counts total vehicle in database
def addDB():
    conn = startDB()
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM Location")
    result = cursor.fetchone()[0]
    return result
    cursor.close()


# park button
def park():
    # database()
    loci()
    aval()
    disp()  # display parking slots on GUI


# Delete vehicle from database
def deleteDB():
    try:

        conn = startDB()
        cursor = conn.cursor()
        name = vehicle.get()
        try:
            mob = mobi.get()
        except:
            msg = messagebox.showinfo("Error!!!", "Please Enter a valid Number")
            mob = 0
        try:
            sql_select_query = """SELECT * from Location where Vehicle= ? AND Contact=?"""
            cursor.execute(sql_select_query, (name, mob))
            row = cursor.fetchall()
            while row:
                a1 = row[0][2]
                b1 = row[0][3]
                break
            # update location on map for filling
            global rl
            df = pd.read_csv('Data' + os.path.sep + "map_grid.csv", header=None)
            df.dropna(axis=0)
            temp = df.values.tolist()
            temp[a1][b1] = 'E'
            pd.DataFrame(temp).to_csv('Data' + os.path.sep + "map_grid.csv", header=None, index=False)
            for i in temp:
                print(i)
            print("*******EOL******")

            sql_delete_query = """DELETE from Location where Vehicle= ? AND Contact=?"""
            cursor.execute(sql_delete_query, (name, mob))

            conn.commit()
            cursor.close()
            aval()  # update available slots
            disp()  # display available slots
        except sqlite3.Error as error:
            msg1 = messagebox.showinfo("Delete Failed", "Vehicle does not Exist")


    except Exception as error:
        msg4 = messagebox.showinfo("Delete Failed", "Vehicle not found")
    finally:
        if (conn):
            conn.close()


# give location from database
def findLoc():
    try:
        conn = startDB()
        cursor = conn.cursor()
        name = vehicle.get()
        mob = mobi.get()
        sql_select_query = """SELECT * from Location where Vehicle= ? AND Contact=?"""
        cursor.execute(sql_select_query, (name, mob))
        row = cursor.fetchall()
        flag = 1
        while row:
            flag = 0
            msg = messagebox.showinfo("Vehicle Found", "Vehicle parked at (%d,%d)" % (row[0][2], row[0][3]))
            disp()
            break
        if (flag == 1):
            msg = messagebox.showinfo("Error!!!", "No Matching Vehicle Found")
        conn.commit()
        cursor.close()

    except Exception as error:
        msg5 = messagebox.showinfo("Error!!!", error)

    finally:
        if (conn):
            conn.close()


# update available slots
def aval():
    global toll
    o = 0
    p = addDB()
    o = toll - p

    avl2 = Label(root, text=o, padx=60, pady=20, fg="white", font=(20), bg="#263D42")
    avl2.place(x=330, y=170)


# close application
def action():
    msg = messagebox.showinfo("Finished!!!", "Thank You for using AIA Parking Management Software ")
    root.destroy()
    # shut()
