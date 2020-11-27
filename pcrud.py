from tkinter import *
import tkinter
from tkinter import messagebox
import pymysql
import data

windo = tkinter.Tk()

windo.geometry("700x450")

L = Label(windo, text="Enter First Name:", font=('arial', 30), fg='blue')
L.grid(row=0, column=0)
E = Entry(windo, bd=5, width=50)
E.grid(row=0, column=1)

L1 = Label(windo, text="Enter Last Name:", font=('arial', 30), fg='blue')
L1.grid(row=1, column=0)
E1 = Entry(windo, bd=5, width=50)
E1.grid(row=1, column=1)

L2 = Label(windo, text="Enter Age:", font=('arial', 30), fg='blue')
L2.grid(row=2, column=0)
E2 = Entry(windo, bd=5, width=50)
E2.grid(row=2, column=1)

host1=data.host
name1=data.name
password1=data.password
database_name1=data.database_name

def myButtonEvent(selection):
    print("First Name is : ", E.get())
    print("Last Name is : ", E1.get())
    print("Age is : ", E2.get())

    fname = E.get()
    lname = E1.get()
    age = E2.get()

    if selection in ('Insert'):
        
        con = pymysql.connect(host1,name1,password1,database_name1)  # connect to mysql
        cur = con.cursor()  # get the cursor object

        createTableQuery='''create table if not exists random (fname varchar(255),
                        lname varchar(255),age int)'''
        
        cur.execute(createTableQuery)
        con.commit()

        insertQuery = "insert into users(fname,lname,age) values ('%s','%s','%s')" % (
            fname, lname, age)
        try:
            cur.execute(insertQuery)
            con.commit()
            print("Data inserted into users table successfully.")
            con.close()
        except Exception as e:
            print("Error occured at data insertion ", e)
            con.rollback()
            con.close()
    elif selection in ('Update'):
        con = pymysql.connect(host1,name1,password1,database_name1)  # connect to mysql
        cur = con.cursor()  # get the cursor object
        updateQuery="update users set \
                    fname='%s' "%(fname)+", lname='%s' "%(lname)+"\
                    where age='%s'" % (age)
        try:
            cur.execute(updateQuery)
            con.commit()
            con.close()
            print("Data Updated into users table successfully..")
        except Exception as e:
            print("Error occured at data insertion ", e)
            con.rollback()
            con.close()
    elif selection in ('Delete'):
        con = pymysql.connect(host1,name1,password1,database_name1)  # connect to mysql
        cur = con.cursor()  # get the cursor object
        deleteQuery=''' delete from users
                    where fname='%s' '''%(fname)
        try:
            cur.execute(deleteQuery)
            con.commit()
            con.close()
            print("Data Deleted from users table successfully..")
        except Exception as e:
            print("Error occured at data deletion..", e)
            con.rollback()
            con.close()
    elif selection in ('Select'):
        con = pymysql.connect(host1, name1, password1,
                              database_name1)  # connect to mysql
        cur = con.cursor()  # get the cursor object
        selectQuery='''select * from users
                    where fname='%s' '''%(fname)
        try:
            cur.execute(selectQuery)
            rows=cur.fetchall()
            fname1=''
            lname1=''
            age1=''
            for row in rows:
                fname1=row[0]
                lname1=row[1]
                age1=row[2]
            E.delete(0,END)
            E1.delete(0,END)
            E2.delete(0,END)

            E.insert(0,fname1)
            E1.insert(0,lname1)
            E2.insert(0,age1)
            con.close()
            print("Data selected from users table successfully..")
        except Exception as e:
            print("Error occured at data selection..", e)
            
            con.close()


BInsert = tkinter.Button(text='Insert', fg='black', bg='orange',
                         font=('arial', 20, 'bold'), command=lambda: myButtonEvent("Insert"))
BInsert.grid(row=5, column=0)

BUpdate = tkinter.Button(text='Update', fg='blue', bg='yellow',
                         font=('arial', 20, 'bold'),command=lambda: myButtonEvent("Update"))
BUpdate.grid(row=5, column=1)

BDelete = tkinter.Button(text='Delete', fg='Red', bg='white',
                         font=('arial', 20, 'bold'),command=lambda: myButtonEvent("Delete"))
BDelete.grid(row=7, column=0)

BSelect = tkinter.Button(text='Select', fg='orange', bg='black',
                         font=('arial', 20, 'bold'), command=lambda: myButtonEvent("Select"))
BSelect.grid(row=7, column=1)

mainloop()
