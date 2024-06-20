**SQL Joins**
================

### Types of Joins
#### 1. INNER JOIN
* Returns only the rows that have matching values in both tables.
* Syntax: `SELECT * FROM table1 INNER JOIN table2 ON table1.column_name = table2.column_name;`

#### 2. LEFT JOIN (or LEFT OUTER JOIN)
* Returns all the rows from the left table and the matching rows from the right table.
* If there are no matches, the result set will contain null values.
* Syntax: `SELECT * FROM table1 LEFT JOIN table2 ON table1.column_name = table2.column_name;`

#### 3. RIGHT JOIN (or RIGHT OUTER JOIN)
* Returns all the rows from the right table and the matching rows from the left table.
* If there are no matches, the result set will contain null values.
* Syntax: `SELECT * FROM table1 RIGHT JOIN table2 ON table1.column_name = table2.column_name;`

#### 4. FULL JOIN (or FULL OUTER JOIN)
* Returns all the rows from both tables.
* If there are no matches, the result set will contain null values.
* Syntax: `SELECT * FROM table1 FULL JOIN table2 ON table1.column_name = table2.column_name;`

#### 5. CROSS JOIN
* Returns the Cartesian product of both tables.
* Each row of one table is combined with each row of the other table.
* Syntax: `SELECT * FROM table1 CROSS JOIN table2;`

### Example Queries
```sql
-- INNER JOIN
SELECT *
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;

-- LEFT JOIN
SELECT *
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id;

-- RIGHT JOIN
SELECT *
FROM customers
RIGHT JOIN orders
ON customers.customer_id = orders.customer_id;

-- FULL JOIN
SELECT *
FROM customers
FULL JOIN orders
ON customers.customer_id = orders.customer_id;

-- CROSS JOIN
SELECT *
FROM customers
CROSS JOIN orders;
