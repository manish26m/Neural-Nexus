#### Database Schema

**1. Products Table**
```sql
CREATE TABLE products (
    pid INT(3) PRIMARY KEY,
    pname VARCHAR(50) NOT NULL,
    price INT(10) NOT NULL,
    stock INT(5),
    location VARCHAR(30) CHECK(location IN ('Mumbai', 'Delhi'))
);
```
- Columns: `pid`, `pname`, `price`, `stock`, `location`.
- Constraints: `PRIMARY KEY` on `pid`, `CHECK` constraint on `location`.

**2. Customer Table**
```sql
CREATE TABLE customer (
    cid INT(3) PRIMARY KEY,
    cname VARCHAR(30) NOT NULL,
    age INT(3),
    addr VARCHAR(50)
);
```
- Columns: `cid`, `cname`, `age`, `addr`.
- Constraints: `PRIMARY KEY` on `cid`.

**3. Orders Table**
```sql
CREATE TABLE orders (
    oid INT(3) PRIMARY KEY,
    cid INT(3),
    pid INT(3),
    amt INT(10) NOT NULL,
    FOREIGN KEY(cid) REFERENCES customer(cid),
    FOREIGN KEY(pid) REFERENCES products(pid)
);
```
- Columns: `oid`, `cid`, `pid`, `amt`.
- Constraints: `PRIMARY KEY` on `oid`, `FOREIGN KEY` on `cid` and `pid`.

**4. Payment Table**
```sql
CREATE TABLE payment (
    pay_id INT(3) PRIMARY KEY,
    oid INT(3),
    amount INT(10) NOT NULL,
    mode VARCHAR(30) CHECK(mode IN ('upi', 'credit', 'debit')),
    status VARCHAR(30),
    FOREIGN KEY(oid) REFERENCES orders(oid)
);
```
- Columns: `pay_id`, `oid`, `amount`, `mode`, `status`.
- Constraints: `PRIMARY KEY` on `pay_id`, `CHECK` constraint on `mode`, `FOREIGN KEY` on `oid`.

#### TCL Commands

**1. Commit**
- Permanently saves a transaction to the database.
```sql
COMMIT;
```

**2. Rollback**
- Reverts changes made by a transaction that hasn’t been saved to the database.
```sql
ROLLBACK;
```

**3. Savepoint**
- Temporarily saves a transaction for later rollback.
```sql
SAVEPOINT a;
ROLLBACK TO a;
```

#### Triggers

**1. Trigger to Update Payment Status After Order is Completed**
```sql
DELIMITER //
CREATE TRIGGER update_payment_status
AFTER UPDATE ON orders
FOR EACH ROW
BEGIN
    IF NEW.status = 'completed' THEN
        UPDATE payment
        SET status = 'completed'
        WHERE oid = NEW.oid;
    END IF;
END //
DELIMITER ;
```

**2. Trigger to Check Stock Availability Before Inserting an Order**
```sql
DELIMITER //
CREATE TRIGGER check_stock_before_order
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE available_stock INT;
    SELECT stock INTO available_stock FROM products WHERE pid = NEW.pid;
    IF available_stock < NEW.amt THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Insufficient stock for this product';
    END IF;
END //
DELIMITER ;
```

**3. Trigger to Update Stock After an Order is Placed**
```sql
DELIMITER //
CREATE TRIGGER update_stock_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE products
    SET stock = stock - NEW.amt
    WHERE pid = NEW.pid;
END // 
DELIMITER ;
```

#### Views

**1. Create a View to Display Customers with Their Corresponding Orders**
```sql
CREATE VIEW CustomerOrders AS
SELECT c.cid, c.cname, o.oid, o.amt, p.pname
FROM customer c
JOIN orders o ON c.cid = o.cid
JOIN products p ON o.pid = p.pid;
```

**2. Create or Replace a View to Show Payment Details with Order and Customer Information**
```sql
CREATE OR REPLACE VIEW payment_order_customer_details AS
SELECT p.pay_id, p.oid, o.cid, c.cname, c.age, c.addr, p.amount, p.mode, p.status
FROM payment p
JOIN orders o ON p.oid = o.oid
JOIN customer c ON o.cid = c.cid;
```

**3. Drop a View if it Exists**
```sql
DROP VIEW IF EXISTS payment_order_customer_details;
```

### Notes Summary

- **TCL Commands**: Used to manage transactions and ensure the consistency and durability of data.
- **Triggers**: Automatically execute predefined actions on specific database events (insert, update, delete).
- **Views**: Virtual tables created by querying one or more tables, useful for simplifying complex queries and enhancing security.
- **Key Constraints and Clauses**: Ensuring data integrity through primary keys, foreign keys, check constraints, and other SQL features.
- **Best Practices**: Regularly use transactions to ensure data integrity, validate data before modifications using triggers, and use views for simplifying data access and improving security.
