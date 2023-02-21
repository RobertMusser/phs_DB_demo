
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost/MAMP",
    user="user",
    password="password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE phs_test")

