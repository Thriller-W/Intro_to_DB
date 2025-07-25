import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connecting to MySQL Server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Powerauthoritycr@25'
        )

        # Creating a cursor object to interact with the server
        cursor = connection.cursor()

        # SQL statement to create the database
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

        # Execute the SQL command
        cursor.execute(create_db_query)

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print("Error: Could not connect or execute command.")
        print(f"Details: {err}")

    finally:
        # Ensure the connection is closed
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
