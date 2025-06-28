/*
6. Populating Your Database with Your More Data
mandatory
Write a script that inserts multiple rows in the table customer (database alx_book_store) in your MySQL server.

Data insertion

    - `customer_id` = `2`
    - `customer_name` = `Blessing Malik`
    - `email` = `bmalik@sandtech.com`
    - `address` = `124 Happiness  Ave.`

    - `customer_id` = `3`
    - `customer_name` = `Obed Ehoneah`
    - `email` = `eobed@sandtech.com`
    - `address` = `125 Happiness  Ave.`

    - `customer_id` = `4`
    - `customer_name` = `Nehemial Kamolu`
    - `email` = `nkamolu@sandtech.com`
    - `address` = `126 Happiness  Ave.`
    
The database name will be passed as an argument of the mysql command

The name of the file should be task_6.sql
*/
-- task_6.sql

-- Use the alx_book_store database
USE alx_book_store;

-- Insert multiple rows into the Customers table
INSERT INTO customer (customer_id, customer_name, email, address) VALUES
(2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
(3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
(4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.');
