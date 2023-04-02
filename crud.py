import mysql.connector

# Connect to the SQL server
try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user = "root",
        password = "2468",
        database = "Flight_Dashboard"
    )
    mycursor = conn.cursor()
    print("Connection Successful")
except:
    print("Connection Failed")

