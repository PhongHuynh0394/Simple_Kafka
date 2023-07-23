import mysql.connector
from time import sleep

while True:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='0409', #base on env file
        database='my_database'
    )
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM livetolldata')

    # Fetch the result set
    result = cursor.fetchall()

    # Process the result as needed
    for row in result:
        print(row)
    sleep(3)