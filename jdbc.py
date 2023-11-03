import mysql.connector

# Replace these variables with your MySQL database credentials
host = 'localhost'
user = 'root'
password = 'root'
database = 'test'

# Establish a connection to the MySQL server
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    if connection.is_connected():
        print("Connected to MySQL database")

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Execute a SELECT query
        cursor.execute("SELECT * FROM employee")

        # Fetch and print the result
        records = cursor.fetchall()
        for record in records:
            print(record)

        # Close the cursor and connection
        cursor.close()
        connection.close()

except mysql.connector.Error as e:
    print(f"Error: {e}")
