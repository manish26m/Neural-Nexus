
# Data Query Language (DQL)

DQL primarily involves the SQL commands used to retrieve data from a database. The main command used in DQL is `SELECT`.

## SELECT Statements

- **Basic SELECT Statement:**
  ```sql
  SELECT column1, column2 FROM table_name;
  ```
  This retrieves specific columns from a table.

- **Selecting All Columns:**
  ```sql
  SELECT * FROM table_name;
  ```
  The asterisk (*) selects all columns from the specified table.

- **Using WHERE Clause:**
  ```sql
  SELECT column1, column2 FROM table_name WHERE condition;
  ```
  Filters the results based on the given condition.

- **Ordering Results:**
  ```sql
  SELECT column1, column2 FROM table_name ORDER BY column1 ASC|DESC;
  ```
  Orders the results in ascending or descending order based on the specified column.

- **Using DISTINCT Keyword:**
  ```sql
  SELECT DISTINCT column1 FROM table_name;
  ```
  Retrieves unique values from the specified column.

- **LIMIT Clause:**
  ```sql
  SELECT column1, column2 FROM table_name LIMIT number;
  ```
  Limits the number of rows returned by the query.

## Complex Queries

- **Joins:**
  - **INNER JOIN:** Selects records with matching values in both tables.
    ```sql
    SELECT columns FROM table1 INNER JOIN table2 ON table1.common_column = table2.common_column;
    ```
  - **LEFT JOIN (or LEFT OUTER JOIN):** Selects all records from the left table and matched records from the right table.
    ```sql
    SELECT columns FROM table1 LEFT JOIN table2 ON table1.common_column = table2.common_column;
    ```
  - **RIGHT JOIN (or RIGHT OUTER JOIN):** Selects all records from the right table and matched records from the left table.
    ```sql
    SELECT columns FROM table1 RIGHT JOIN table2 ON table1.common_column = table2.common_column;
    ```

- **Subqueries:**
  - **Single-row Subquery:**
    ```sql
    SELECT column1 FROM table_name WHERE column2 = (SELECT column2 FROM table_name2 WHERE condition);
    ```
  - **Multiple-row Subquery:**
    ```sql
    SELECT column1 FROM table_name WHERE column2 IN (SELECT column2 FROM table_name2 WHERE condition);
    ```
  - **Correlated Subquery:** References columns from the outer query.
    ```sql
    SELECT column1 FROM table1 t1 WHERE column2 > (SELECT AVG(column2) FROM table1 t2 WHERE t1.common_column = t2.common_column);
    ```

## Advanced Functions

- **Aggregate Functions:**
  - **SUM:** Calculates the total sum of a numeric column.
    ```sql
    SELECT SUM(column_name) FROM table_name;
    ```
  - **AVG:** Calculates the average value of a numeric column.
    ```sql
    SELECT AVG(column_name) FROM table_name;
    ```
  - **COUNT:** Returns the number of rows that match a specified condition.
    ```sql
    SELECT COUNT(column_name) FROM table_name WHERE condition;
    ```

- **String Functions:**
  - **CONCAT:** Concatenates two or more strings.
    ```sql
    SELECT CONCAT(column1, column2) FROM table_name;
    ```

- **Date Functions:**
  - **NOW():** Returns the current date and time.
    ```sql
    SELECT NOW();
    ```
  - **DATE_FORMAT:** Formats a date value based on the specified format.
    ```sql
    SELECT DATE_FORMAT(column_name, '%Y-%m-%d') FROM table_name;
    ```

