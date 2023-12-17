import mysql.connector
from random import randint, choice
import random
from datetime import datetime, timedelta

def random_date(start_date, end_date):
    time_delta = end_date - start_date
    random_days = random.randint(0, time_delta.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date

# Example usage
start_date = datetime(2015, 1, 1)
end_date = datetime(2030, 1, 1)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sentry2703",
    database="airport"
)

print(connection)

cursor = connection.cursor()

select_query = "SELECT idPlane FROM Plane;"
cursor.execute(select_query)
rows = cursor.fetchall()

plane_list = [row[0] for row in rows]

insert_query = "INSERT INTO Flight (idFlight, destination, planeID, departureDate, departureTime, flightTime) VALUES (%s, %s, %s, %s, %s, %s)"

for i in range(4, 400):
    row = []
    row.append("FL" + str(i).zfill(3));
    row.append(choice(["Los Angeles, California", "New York", "Chicago, Illinois", "Miami, Florida", "Houston, Texas", "Phoenix, Arizona", "Philadelphia", "San Antonio", "San Diego, California", "Dallas Texas"]))
    row.append(choice(plane_list))
    row.append(random_date(start_date, end_date))
    row.append("12:00:00")
    row.append(randint(100, 2000))

    cursor.execute(insert_query, row)

connection.commit()
cursor.close()
connection.close()