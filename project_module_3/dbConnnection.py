import mysql.connector


def db_connection():
  mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="ali123"
) 


