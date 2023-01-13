import mysql.connector as sqlcon
mydb=sqlcon.connect(host="localhost", user="root", password="student", database="reportcards")

from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.configure(background="white")
root.title("Report Card")
root.geometry("500x200")
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)


if mydb.is_connected():
    print("success")

mycursor=mydb.cursor()


def clearscreen():
    for label in root.grid_slaves():
        label.grid_forget()
    
    root.geometry("500x200")

    homebutton = Button(root, text="Go Home", command=gohome)
    homebutton.grid(row=0, column=0, columnspan=2)


def choice1():

    clearscreen()

    root.geometry("800x300")

    Label(root, text="Enter and save a student's details ➡", font= ('Helvetica 15 underline'), bg="white").grid(row=1, column=0)

    Label(root, text="Name: ", bg="white").grid(row=2, column=0)
    name=StringVar()
    nameenter=Entry(root, textvariable=name)
    nameenter.grid(row=2, column=1)

    Label(root, text="Roll Number: ", bg="white").grid(row=3, column=0)
    rollno=StringVar()
    rnenter=Entry(root, textvariable=rollno)
    rnenter.grid(row=3, column=1)

    Label(root, text="Physics Marks: ", bg="white").grid(row=4, column=0)
    phym=StringVar()
    phyenter=Entry(root, textvariable=phym)
    phyenter.grid(row=4, column=1)
    
    Label(root, text="Chemistry Marks: ", bg="white").grid(row=5, column=0)
    chemm=StringVar()
    chementer=Entry(root, textvariable=chemm)
    chementer.grid(row=5, column=1)

    Label(root, text="Maths Marks: ", bg="white").grid(row=6, column=0)
    mathm=StringVar()
    mathenter=Entry(root, textvariable=mathm)
    mathenter.grid(row=6, column=1)
    
    Label(root, text="English Marks: ", bg="white").grid(row=7, column=0)
    engm=StringVar()
    engenter=Entry(root, textvariable=engm)
    engenter.grid(row=7, column=1)

    Label(root, text="Computer Science Marks: ", bg="white").grid(row=8, column=0)
    csm=StringVar()
    csenter=Entry(root, textvariable=csm)
    csenter.grid(row=8, column=1)


    def inputFinally():

        if name.get()=="" or rollno.get()=="" or phym.get()=="" or chemm.get()=="" or mathm.get()=="" or engm.get()=="" or csm.get()=="":
            donelabel["text"]="Invalid or Missing Details"

        else:
            mycursor.execute(
                "insert into report(rollno,name,phym,chemm,mathm,engm,csm) values('" + str(rollno.get()) + "','" + str(name.get()) + "','" + str(phym.get()) + "','" + str(chemm.get()) + "','" + str(mathm.get()) + "','"+str(engm.get())+"','"+str(csm.get())+"')")

            mydb.commit()

            donelabel["text"]="student details inputed"

    done=Button(root,text="submit details", command=inputFinally)
    done.grid(row=9, column=0, columnspan=2)
    donelabel = Label(root, text="", bg="white")
    donelabel.grid(row=10, column=0, columnspan=2)


def choice2():

    clearscreen()
    root.geometry("700x800")

    img = ImageTk.PhotoImage(Image.open("logo.jpg"))  

    imagework=Label(root,image=img)
    imagework.image=img
    imagework.grid(row=1, column=0, columnspan=2, sticky=N)

    Label(root, text="Report Card", bg="white", font= ('Helvetica 15 underline')).grid(row=2, column=0, columnspan=2, sticky=N)

    Label(root, text="Enter student roll number: ", bg="white").grid(row=3, column=0)
    rollno = StringVar()
    rollno1 = Entry(root, textvariable=rollno)
    rollno1.grid(row=3, column=1)

    line1=Label(root, text="============================================================", bg="white")
    line1.grid(row=4, column=0,columnspan=2,sticky=N)

    def makecard():
        
        mycursor.execute("select * from report where rollno='"+rollno.get()+"'")
        rec1 = mycursor.fetchone()

        if rec1==None:
            line1["text"]="student not found"
        
        else:

            line1["text"]="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

            Label(root, text="Roll Number: ", bg="white").grid(row=5,column=0)
            Label(root, text=rec1[0], bg="white").grid(row=5,column=1)
            Label(root, text="Name: ", bg="white").grid(row=6,column=0)
            Label(root, text=rec1[1], bg="white").grid(row=6,column=1)
            Label(root, text="Physics Marks: ", bg="white").grid(row=7,column=0)
            Label(root, text=rec1[2], bg="white").grid(row=7,column=1)
            Label(root, text="Chemistry Marks: ", bg="white").grid(row=8,column=0)
            Label(root, text=rec1[3], bg="white").grid(row=8,column=1)
            Label(root, text="Maths Marks: ", bg="white").grid(row=9,column=0)
            Label(root, text=rec1[4], bg="white").grid(row=9,column=1)
            Label(root, text="English Marks: ", bg="white").grid(row=10,column=0)
            Label(root, text=rec1[5], bg="white").grid(row=10,column=1)
            Label(root, text="Computer Science Marks: ", bg="white").grid(row=11,column=0)
            Label(root, text=rec1[6], bg="white").grid(row=11,column=1)

            dowork.destroy()

    dowork=Button(root, text="generate", command=makecard)
    dowork.grid(row=12, column=0, columnspan=2)



def gohome():
    clearscreen()

    header = Label(root, text="~~Report Card Creator~~", bg="white")
    header.grid(row=1, column=0, columnspan=2)

    line1 = Label(root, bg="white", text="-----------------------------------------------------------")
    line1.grid(row=2, column=0, columnspan=2)

    bchoice1 = Button(root, text="1. enter and save a student's details", command=choice1)
    bchoice1.grid(row=3, column=0)
    bchoice2 = Button(root, text="2. generate a student's report card", command=choice2)
    bchoice2.grid(row=3, column=1)

    line2 = Label(root, bg="white", text="------------------------------------------------------------")
    line2.grid(row=4, column=0, columnspan=2)


gohome()

homebutton=Button(root, text="Go Home", command=gohome)
homebutton.grid(row=0, column=0, columnspan=2)

root.mainloop()
