/*
5. Populating Your Database with Your Very First Data
mandatory
Write a script that inserts a single row in the table customer (database alx_book_store) in your MySQL server.

Singel data insertion

customer_id = 1
customer_name = Cole Baidoo
email = cbaidoo@sandtech.com
address = 123 Happiness Ave.
The database name will be passed as an argument of the mysql command

Name of the file should be task_5.sql

All SQL keywords should be in uppercase
*/
-- task_5.sql

-- Use the alx_book_store database
USE alx_book_store;

-- Insert a single row into the Customers table
INSERT INTO customer (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');
