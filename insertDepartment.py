import mysql.connector
from random import randint, choice
from Reader import *

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sentry2703"
)

print(connection)

cursor = connection.cursor()

sample_data = read()

cursor.execute("use airport;")

insert_query = "INSERT INTO Department (idDepartment, positionName, classification, primaryLocation) VALUES (%s, %s, %s, %s)"

for dict in my_list:
    row = []
    for k, v in dict.items():
        if (k == "idDepartment"):
            row.append(int(v))
        else:
            row.append(v)
    cursor.execute(insert_query, row)

connection.commit()

cursor.close()
connection.close()
