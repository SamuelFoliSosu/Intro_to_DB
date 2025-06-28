/*
4. Full description
mandatory
Write a script that prints the full description of the table books from the database alx_book_store in your MySQL server.

The database name will be passed as an argument of the mysql command
You are not allowed to use the DESCRIBE or EXPLAIN statements
The name of the file should be task_4.sql
All SQL keywords should be in uppercase
*/
-- task_4.sql

-- Use the alx_book_store database
USE alx_book_store;

-- Retrieve full column details for the 'Books' table from INFORMATION_SCHEMA.COLUMNS.
-- This effectively provides a "full description" without using DESCRIBE or EXPLAIN.
SELECT
    COLUMN_NAME AS Field,
    COLUMN_TYPE AS Type,
    IS_NULLABLE AS Null,
    COLUMN_KEY AS 'Key',
    COLUMN_DEFAULT AS 'Default',
    EXTRA AS Extra
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books'
ORDER BY
    ORDINAL_POSITION;
