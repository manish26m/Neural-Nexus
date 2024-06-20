**Database Normalization**
=========================

### Normalization Rules
#### Why Normalize?
* Eliminate data redundancy
* Reduce data inconsistencies
* Improve data integrity
* Simplify data management

### First Normal Form (1NF)
#### Definition
A table is in 1NF if all columns contain **atomic values** (single value).

#### Rules
* Each table cell must contain a **single value**.
* Each column must have a **unique name**.

### Second Normal Form (2NF)
#### Definition
A table is in 2NF if it is in 1NF and all **non-prime attributes** are **fully functionally dependent** on the **primary key**.

#### Rules
* A table must be in 1NF.
* All non-prime attributes must depend on the **entire primary key**.

### Third Normal Form (3NF)
#### Definition
A table is in 3NF if it is in 2NF and there are **no transitive dependencies**.

#### Rules
* A table must be in 2NF.
* If A → B and B → C, then A → C (**no transitive dependencies**).

### Higher Normal Forms
#### Boyce-Codd Normal Form (BCNF)
* A table is in BCNF if it is in 3NF and there are **no transitive dependencies**.

#### Fourth Normal Form (4NF)
* A table is in 4NF if it is in BCNF and there are **no multi-level dependencies**.

#### Fifth Normal Form (5NF)
* A table is in 5NF if it is in 4NF and there are **no join dependencies**.
