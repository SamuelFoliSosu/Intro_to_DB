"""
1. Let's Build Your Database: Your Gateway to Data Adventure!
mandatory
Write a simple python script that creates the database alx_book_store in your MySQL server.

Name of python script should be MySQLServer.py
If the database alx_book_store already exists, your script should not fail
You are not allowed to use the -- or -- statements
NOTE :

Required to print message such as Database 'alx_book_store' created successfully! when database is successfully created.

Print error message to handle errors when failing to connect to the DB.

handle open and close of the DB in your script.
"""

"""
# MySQLServer.py

import mysql.connector

def create_database():
"""
#Connects to MySQL server and creates the 'alx_book_store' database
#if it doesn't already exist.
"""
    try:
        # Establish a connection to the MySQL server
        # Replace 'your_user', 'your_password', and 'your_host' with your MySQL credentials
        conn = mysql.connector.connect(
            host="localhost",  # Or your MySQL host
            user="root",     # Your MySQL username
            password=""  # Your MySQL password
        )

        if conn.is_connected():
            cursor = conn.cursor()

            # SQL statement to create the database if it doesn't exist
            # This statement does NOT use  or  keywords explicitly.
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_db_query)

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # Handle connection errors or other MySQL errors
        # Specifically, if the database creation fails for any reason
        # (e.g., permissions, invalid name), it will be caught here.
        print(f"Error: Failed to connect to the DB or create database: {err}")

    finally:
        # Ensure the connection is closed even if an error occurs
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    create_database()
"""

# MySQLServer.py

import mysql.connector

def create_database():
    """
    Connects to MySQL server and attempts to create the 'alx_book_store' database.
    Handles the case where the database already exists by checking the error message string.
    """
    conn = None
    cursor = None
    try:
        # Establish a connection to the MySQL server
        # Replace 'your_user', 'your_password', and 'your_host' with your MySQL credentials
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        if conn.is_connected():
            cursor = conn.cursor()

            # Attempt to create the database directly.
            # This will raise an error if the database already exists.
            create_db_query = "CREATE DATABASE alx_book_store"
            cursor.execute(create_db_query)

            # This print statement will only be reached if the database was actually created
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # Check if the error message contains "database exists" (common for error 1007)
        # This avoids using specific error codes or IF NOT EXISTS.
        if "database exists" in str(err).lower():
            # If the database already exists, we do nothing and print nothing,
            # as no specific output was requested for this case, and the script must not fail.
            pass
        else:
            # Handle other connection or database creation errors (e.g., permission denied)
            print(f"Error: Failed to connect to the DB or create database: {err}")

    finally:
        # Ensure the cursor and connection are closed properly
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    create_database()