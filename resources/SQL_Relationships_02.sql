--* Types of Relationships

In SQL, tables are used to store data in a structured way. A database can contain multiple tables, and these tables can be related to each other.

There are three main types of relationships between tables in SQL:

1. One-to-One Relationship:

In a one-to-one relationship, each record in one table is associated with exactly one record in another table. Let's say we have two tables: `employees` and `employee_addresses`. The `employees` table has a primary key called `employee_id`, and the `employee_addresses` table has a primary key called `address_id` and a foreign key called `employee_id`.

Here's what the relationship would look like visually:

```
+-------------+               +--------------------+
|  employees  |               | employee_addresses |
+-------------+               +--------------------+
| employee_id | <---(1:1)---> | employee_id        |
| name        |               | address_id         |
| email       |               | address            |
| phone       |               +--------------------+
+-------------+
```

As you can see, each record in the `employees` table is associated with exactly one record in the `employee_addresses` table, and vice versa.

2. One-to-Many Relationship:

In a one-to-many relationship, each record in one table can be associated with many records in another table. Let's say we have two tables: `customers` and `orders`. The `customers` table has a primary key called `customer_id`, and the `orders` table has a primary key called `order_id` and a foreign key called `customer_id`.

Here's what the relationship would look like visually:

```
+-------------+               +-------------+
|  customers  |               |   orders    |
+-------------+               +-------------+
| customer_id | <---(1:M)---> | customer_id |
| name        |               | order_id    |
| email       |               | date        |
| phone       |               +-------------+
+-------------+
```

As you can see, each record in the `customers` table can be associated with many records in the `orders` table, but each record in the `orders` table can only be associated with one record in the `customers` table.

3. Many-to-Many Relationship:

In a many-to-many relationship, each record in one table can be associated with many records in another table, and vice versa. Let's say we have two tables: `students` and `classes`. Since a student can be enrolled in many classes and a class can have many students, we need to use a third table, called a junction or mapping table, which contains foreign keys from both tables. We'll call this table `enrollments`.

Here's what the relationship would look like visually:

```
+-------------+               +-------------+               +-------------+
|   students  |               | enrollments |               |   classes   |
+-------------+               +-------------+               +-------------+
|  student_id | <---(M:M)---> |  student_id | <---(M:M)---> |  class_id   |
|     name    |               |  class_id   |               |    name     |
|    email    |               +-------------+               | description |
|    phone    |                                             +-------------+
+-------------+
```

As you can see, each record in the `students` table can be associated with many records in the `classes` table, and vice versa. The `enrollments` table serves as a mapping between the two tables, and contains foreign keys from both tables.

In SQL, you can combine data from multiple tables by using JOINs. JOINs allow you to combine rows from two or more tables based on a related column or key.

--* JOINS

Here's an example to illustrate how to combine data from multiple tables using JOINs:

Let's say you have two tables: `customers` and `orders`. The `customers` table contains information about your customers, such as their name and email address, and has a primary key called `customer_id`. The `orders` table contains information about customer orders, such as the order date and total amount, and has a foreign key called `customer_id` that relates each order to a customer in the `customers` table.

Here's what the tables might look like:

```
+-------------+               +-------------+
|  customers  |               |   orders    |
+-------------+               +-------------+
| customer_id |               | order_id    |
| name        |               | order_date  |
| email       |               | total_amount|
| phone       |               | customer_id |
+-------------+               +-------------+
```

To combine data from these two tables, you can use a JOIN statement like this:

```
SELECT customers.name, orders.order_date, orders.total_amount
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id;
```

This statement selects the `name`, `order_date`, and `total_amount` columns from the `customers` and `orders` tables, and joins them together based on the `customer_id` column.

By using JOINs to combine data from multiple tables, you can keep your data DRY (Don't Repeat Yourself) and normalized. Normalization is the process of organizing data in a database so that it is free from redundant data and logical errors. By normalizing your data, you can avoid data inconsistencies and improve data integrity.


--* Different Types of Joins

SQL joins are used to combine data from two or more tables based on a common column between them. Here are the different types of joins:

1. Inner Join: Inner join returns only the matching records between two tables.

Example:

```
SELECT *
FROM Table1
INNER JOIN Table2
ON Table1.column_name = Table2.column_name;
```

In the above code, `Table1` and `Table2` are the names of the tables being joined, and `column_name` is the common column between the two tables. The `INNER JOIN` keyword is used to perform an inner join between the two tables. The result set will only include the rows where there is a match between the two tables on the specified column.

2. Left Join: Left join returns all records from the left table and matching records from the right table.

Example:

```
SELECT *
FROM Table1
LEFT JOIN Table2
ON Table1.column_name = Table2.column_name;
```

In the above code, `Table1` and `Table2` are the names of the tables being joined, and `column_name` is the common column between the two tables. The `LEFT JOIN` keyword is used to perform a left join between the two tables. The result set will include all rows from `Table1`, and the matching rows from `Table2`. If there are no matching rows in `Table2`, the result set will include NULL values for the columns in `Table2`.

3. Right Join: Right join returns all records from the right table and matching records from the left table.

Example:

```
SELECT *
FROM Table1
RIGHT JOIN Table2
ON Table1.column_name = Table2.column_name;
```

In the above code, `Table1` and `Table2` are the names of the tables being joined, and `column_name` is the common column between the two tables. The `RIGHT JOIN` keyword is used to perform a right join between the two tables. The result set will include all rows from `Table2`, and the matching rows from `Table1`. If there are no matching rows in `Table1`, the result set will include NULL values for the columns in `Table1`.

4. Full Outer Join: Full outer join returns all records from both tables.

Example:

```
SELECT *
FROM Table1
FULL OUTER JOIN Table2
ON Table1.column_name = Table2.column_name;
```

In the above code, `Table1` and `Table2` are the names of the tables being joined, and `column_name` is the common column between the two tables. The `FULL OUTER JOIN` keyword is used to perform a full outer join between the two tables. The result set will include all rows from both tables, and NULL values for any columns where there is no matching row in the other table.

These are the four main types of joins in SQL. It's important to understand the differences between them and choose the appropriate join for your specific use case.