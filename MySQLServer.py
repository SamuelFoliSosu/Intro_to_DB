"""
1. Let's Build Your Database: Your Gateway to Data Adventure!
mandatory
Write a simple python script that creates the database alx_book_store in your MySQL server.

Name of python script should be MySQLServer.py
If the database alx_book_store already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements
NOTE :

Required to print message such as Database 'alx_book_store' created successfully! when database is successfully created.

Print error message to handle errors when failing to connect to the DB.

handle open and close of the DB in your script.
"""
# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

def create_database():
    """
    Connects to MySQL server and attempts to create the 'alx_book_store' database.
    Handles the case where the database already exists by catching a specific error.
    """
    conn = None # Initialize conn to None
    cursor = None # Initialize cursor to None
    try:
        # Establish a connection to the MySQL server
        # Replace 'your_user', 'your_password', and 'your_host' with your MySQL credentials
        conn = mysql.connector.connect(
            host="localhost",  # Or your MySQL host
            user="root",     # Your MySQL username
            password=""      # Your MySQL password
        )

        if conn.is_connected():
            cursor = conn.cursor()

            # Attempt to create the database directly
            # This will raise an error if the database already exists
            create_db_query = "CREATE DATABASE alx_book_store"
            cursor.execute(create_db_query)

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # Check if the error is specifically that the database already exists (Error Code 1007)
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"Database 'alx_book_store' already exists. No new creation needed.")
        else:
            # Handle other connection or database creation errors
            print(f"Error: Failed to connect to the DB or create database: {err}")

    finally:
        # Ensure the connection and cursor are closed
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    create_database()