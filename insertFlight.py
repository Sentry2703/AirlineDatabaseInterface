import mysql.connector
from random import randint, choice
from Reader import *

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql242",
    database="airport"
)

print(connection)

cursor = connection.cursor()

insert_query = "INSERT INTO Flight (idFlight, destination, planeID, departureDate, departureTime, flightTime) VALUES (%s, %s, %s, %s, %s, %s)"

