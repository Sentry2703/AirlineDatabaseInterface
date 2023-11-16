import mysql.connector
from random import randint, choice

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sentry2703"
)

print(connection)

cursor = connection.cursor()
cursor.execute("use airport;")

try:
    select_query = "SELECT crewID FROM Plane;"

    cursor.execute(select_query)
    rows = cursor.fetchall()

    crew_list = [list(row) for row in rows]

    print(crew_list)

    select2_query = "SELECT idEmployee FROM Employee WHERE positionID = 1;"
    select3_query = "SELECT idEmployee FROM Employee WHERE positionID = 2;"

    cursor.execute(select2_query)
    pilots = cursor.fetchall()
    cursor.execute(select3_query)
    attendants = cursor.fetchall()

    pilot_list = [list(row) for row in pilots]
    attendant_list = [list(row) for row in attendants]

    for pilot in pilot_list:
        for crew in crew_list:
            decider = randint(0, 100)
            if decider > 65:
                insert_query = "INSERT INTO Crew (employeeID, crewNo) VALUES (%s, %s);"
                cursor.execute(insert_query, [pilot[0], crew[0]])

    for attendant in attendant_list:
        for crew in crew_list:
            decider = randint(0, 100)
            if decider > 30:
                insert_query = "INSERT INTO Crew (employeeID, crewNo) VALUES (%s, %s);"
                cursor.execute(insert_query, [attendant[0], crew[0]])
except mysql.connector.Error as err:
    print(f"Error: {err}")

connection.commit()
cursor.close()
connection.close()