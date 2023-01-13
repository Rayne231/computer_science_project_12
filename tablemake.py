import mysql.connector as sqlcon
mydb=sqlcon.connect(host="localhost", user="root", password="student")


if mydb.is_connected():
          print("success")

mycursor=mydb.cursor()

try:
    mycursor.execute("CREATE DATABASE reportcards")
    print("Database Created")
except:
    print("***Database exists..Creation of Database not required***")

mycursor.execute("USE reportcards")

try:
    mycursor.execute("""
    create table report(
    rollno varchar(20) NOT NULL,
    name varchar(20) NOT NULL,
    phym varchar(50) NOT NULL,
    chemm varchar(20) NOT NULL,
    mathm varchar(20) NOT NULL,
    engm varchar(20) NOT NULL,
    csm varchar(20) NOT NULL)""")

    print("TABLE CREATED")
except:
    print("***Table exists..Table Creation Not Required***")