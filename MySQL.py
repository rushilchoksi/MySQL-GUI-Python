try:
    import mysql.connector
except ImportError:
    print ("Module not found!")
import webbrowser
import time
import csv
import os

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "root",
  database = "Rushil"
)
mycursor = mydb.cursor()
query = input("Enter your MySQL query: ")
mycursor.execute(query)
result=mycursor.fetchall()
f=open("File.txt","a")
myFile=csv.writer(f)
myFile.writerows(result)
f.close()
print ("\nData successfully fetched!")
os.rename("File.txt","File.html")
print ("Opening HTML page in 3 seconds!")
time.sleep(3)
webbrowser.open("File.html")
time.sleep(5)
os.remove("File.html")
