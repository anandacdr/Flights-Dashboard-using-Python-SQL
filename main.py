import mysql.connector

# connect to the database server
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user = 'root',
        password = '2468',
        database='ananda'  # add this line to select a database
    )
    mycursor = conn.cursor()
    print("Connected to the database server")
except:
    print("Error connecting to the database server")

