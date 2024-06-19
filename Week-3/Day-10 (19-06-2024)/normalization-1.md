## Database Normalization

Database normalization is the process of organizing the fields and tables of a relational database to minimize data redundancy and dependency.

### First Normal Form (1NF)

1. Each table cell must contain a single value.
2. Each column must have a unique name.

### Example of 1NF

#### customer

| id | customer_name | address | 
|----|---------------|---------| 
| 1  | John          | 123 Main| 
| 2  | Jane          | 456 Elm | 

### Second Normal Form (2NF)

1. Meet all the requirements of the 1NF.
2. Each non-prime attribute in a table must depend on the entire primary key.

### Example of 2NF

#### customer

| id | customer_name | 
|----|---------------| 
| 1  | John          | 
| 2  | Jane          | 

#### customer_address

| id | address | 
|----|---------| 
| 1  | 123 Main| 
| 2  | 456 Elm | 

### Third Normal Form (3NF)

1. Meet all the requirements of the 2NF.
2. If a table is in 2NF, and a non-prime attribute depends on another non-prime attribute, then it should be moved to a separate table.

### Example of 3NF

#### customer

| id | customer_name | 
|----|---------------| 
| 1  | John          | 
| 2  | Jane          | 

#### customer_address

| id | customer_id | address | 
|----|-------------|---------| 
| 1  | 1           | 123 Main| 
| 2  | 2           | 456 Elm | 

#### order

| id | customer_id | order_date | 
|----|-------------|------------| 
| 1  | 1           | 2022-01-01 | 
| 2  | 2           | 2022-01-15 | 

### Fourth Normal Form (4NF)

1. Meet all the requirements of the 3NF.
2. There should be no multi-valued dependency.

### Example of 4NF

#### customer

| id | customer_name | location | 
|----|---------------|----------| 
| 2  | John          | Chicago  | 
| 6  | Michelle      | Boston   | 
| 8  | Mark          | Chicago  | 
| 15 | Sarah         | Atlanta  | 

#### customer_operating_system

| id | operating_system | 
|----|------------------| 
| 2  | Windows          | 
| 2  | macOS            | 
| 6  | Windows          | 
| 8  | Linux            | 
| 15 | macOS            | 
| 15 | Windows          | 

## Benefits of Normalization

1. Making updates to a record is easier because it only needs to be done in one place.
2. References to the record can be changed without removing the record.
3. It's easier to keep a history of records over time.
4. It reduces the risk of data entry errors.

## How Does Normalization Impact SQL?

Normalization will likely result in more tables being created and more relationships between the tables.

Benefits of writing SQL on a normalized database:

1. Less data is considered: with multiple smaller tables, there is less data for the database to look through and consider when returning results of a query, compared to tables with more rows and more columns.
2. Faster query performance: with multiple smaller tables, queries can be executed faster.

## Drawbacks of Normalization

1. More complex queries: with more tables, queries can become more complex and harder to write.
2. Slower performance: with more tables, there can be a performance hit when querying the database.
3. More difficult to understand: with more tables, it can be harder for someone to understand the structure of the database.

## Denormalization

Denormalization is the process of adding redundant data to a database to improve performance.

### Benefits of Denormalization

1. Faster performance: with redundant data, queries can be executed faster.
2. Simpler queries: with redundant data, queries can be simpler to write.

### Drawbacks of Denormalization

1. More complex updates: with redundant data, updates can become more complex and harder to write.
2. More storage space: with redundant data, more storage space is required.
3. More difficult to maintain: with redundant data, it can be harder to maintain the database.

## Conclusion

Normalization is a process of organizing data in a database to reduce redundancy and improve data integrity. It involves breaking down data into smaller tables and defining relationships between those tables.

Denormalization is the process of adding redundant data to a database
