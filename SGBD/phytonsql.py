import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="thunder123",
  database="thunder"
)
mydb.close()
