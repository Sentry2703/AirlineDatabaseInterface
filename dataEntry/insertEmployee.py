import mysql.connector
from random import randint, choice
from Reader import *

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql242"
)

print(connection)

cursor = connection.cursor()

sample_data = read()

cursor.execute("use airport;")

insert_query = "INSERT INTO Employee (idEmployee, firstName, lastName, positionID, salary, status) VALUES (%s, %s, %s, %s, %s, %s)"

for dict in my_list:
    row = []
    for k, v in dict.items():
        if (k == "idEmployee" or k == 'positionID' or k == 'salary'):
            row.append(int(v))
        else:
            row.append(v)
    cursor.execute(insert_query, row)

connection.commit()

cursor.close()
connection.close()
