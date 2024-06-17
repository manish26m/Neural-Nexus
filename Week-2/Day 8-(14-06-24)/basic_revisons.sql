-- Introduction to SQL
-- SQL stands for Structured Query Language, used to communicate with databases.
-- SQL is used to perform tasks such as retrieving data from a database or updating data in a database.

-- Types of SQL Commands
-- 1. DDL (Data Definition Language): CREATE, ALTER, DROP
-- 2. DML (Data Manipulation Language): SELECT, INSERT, UPDATE, DELETE
-- 3. DCL (Data Control Language): GRANT, REVOKE
-- 4. TCL (Transaction Control Language): COMMIT, ROLLBACK, SAVEPOINT

-- Creating a Database
CREATE DATABASE my_database;

-- Using a Database
USE my_database;

-- Creating a Table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE,
    hire_date DATE,
    salary DECIMAL(10, 2)
);

-- Inserting Data into a Table
INSERT INTO employees (employee_id, first_name, last_name, birth_date, hire_date, salary)
VALUES (1, 'John', 'Doe', '1980-01-01', '2005-03-15', 60000.00);

-- Selecting Data from a Table
SELECT * FROM employees;

-- Updating Data in a Table
UPDATE employees
SET salary = 65000.00
WHERE employee_id = 1;

-- Deleting Data from a Table
DELETE FROM employees
WHERE employee_id = 1;

-- SQL Data Types
-- Numeric types: INT, DECIMAL, FLOAT
-- String types: CHAR, VARCHAR, TEXT
-- Date and time types: DATE, TIME, DATETIME, TIMESTAMP
-- Other types: BOOLEAN, BLOB

-- Advanced SQL Commands

-- JOIN Operations
-- INNER JOIN: Selects records that have matching values in both tables
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.department_id;

-- LEFT JOIN: Selects all records from the left table and matched records from the right table
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id;

-- RIGHT JOIN: Selects all records from the right table and matched records from the left table
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
RIGHT JOIN departments ON employees.department_id = departments.department_id;

-- FULL JOIN: Selects all records when there is a match in either left or right table
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
FULL OUTER JOIN departments ON employees.department_id = departments.department_id;

-- Subqueries
-- Subqueries are nested queries that provide data to the enclosing query.
SELECT first_name, last_name
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Aggregate Functions
-- COUNT: Returns the number of rows
SELECT COUNT(*) FROM employees;

-- SUM: Returns the total sum of a numeric column
SELECT SUM(salary) FROM employees;

-- AVG: Returns the average value of a numeric column
SELECT AVG(salary) FROM employees;

-- MAX: Returns the highest value in a set
SELECT MAX(salary) FROM employees;

-- MIN: Returns the lowest value in a set
SELECT MIN(salary) FROM employees;

-- Group By and Having Clause
-- GROUP BY groups rows that have the same values into summary rows.
-- HAVING is used to filter records that work on summarized GROUP BY results.
SELECT department_id, COUNT(*), AVG(salary)
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 50000;

-- Indexes
-- Indexes are used to retrieve data from the database more quickly than otherwise.
CREATE INDEX idx_last_name ON employees (last_name);

-- Views
-- A view is a virtual table based on the result-set of an SQL statement.
CREATE VIEW high_earners AS
SELECT first_name, last_name, salary
FROM employees
WHERE salary > 70000;

-- Stored Procedures
-- A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.
DELIMITER //
CREATE PROCEDURE getEmployeeCount()
BEGIN
    SELECT COUNT(*) FROM employees;
END //
DELIMITER ;

-- Calling the Stored Procedure
CALL getEmployeeCount();

-- Transactions
-- A transaction is a unit of work that is performed against a database.
-- COMMIT saves all the transactions to the database.
-- ROLLBACK undoes the transactions.
START TRANSACTION;
UPDATE employees SET salary = salary + 5000 WHERE employee_id = 2;
COMMIT;

START TRANSACTION;
UPDATE employees SET salary = salary - 5000 WHERE employee_id = 2;
ROLLBACK;
