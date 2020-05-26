import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='pritam', password='1234',
                               database='mydb')  # creating a database pointing obj

mycursor = mydb.cursor()  # corsor like an pointer

mycursor.execute("show databases")

print("show list of databases\n")
for i in mycursor:
    print(i)


print("show list of all entries in th student table of mydb database")
mycursor.execute("select * from student")

print("directly printing from cursor\n")
for i in mycursor:
    print(i)

print("fetching all entries to a variable\n")
mycursor.execute("select * from student")
result=mycursor.fetchall()
for i in result:
	print(i)

print("fetching only one element(1st)\n")
mycursor.execute("select * from student")
result=mycursor.fetchone()
for i in result:
	print(i)