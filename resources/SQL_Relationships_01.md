# These steps are for creating one-to-many, one-to-one, and many-to-many relationships.

**Creating a Database:**

To create a database, we use the `CREATE DATABASE` statement. Here's an example:

```
CREATE DATABASE myCompany;
```

This creates a new database named "myCompany".

**Connecting to Database:**

```
\c myCompany
```

This connects you to the database you just created.

**Creating Tables:**

Tables are used to store data in a database. To create a table, we use the `CREATE TABLE` statement. Here's an example:

```
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    salary DECIMAL(10,2)
);
```

This creates a table named "employees" with four columns: "id", "name", "age", and "salary". The "id" column is the primary key of the table.

**Creating Relationships:**

In a relational database, tables can have relationships with each other. There are three types of relationships: one-to-one, one-to-many, and many-to-many.

To create a relationship between two tables, we use foreign keys. A foreign key is a column in one table that refers to the primary key of another table.

**One-to-Many Relationship:**

```
CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    salary DECIMAL(10,2),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
```

This creates two tables: "departments" and "employees". The "employees" table has a foreign key column named "department_id" that refers to the primary key of the "departments" table. This establishes a one-to-many relationship between the two tables.

**Example Usage:**

To insert data into the tables, you can use the `INSERT INTO` statement:

```
INSERT INTO departments (id, name) VALUES (1, 'Sales');
INSERT INTO departments (id, name) VALUES (2, 'Marketing');

INSERT INTO employees (id, name, age, salary, department_id) VALUES (1, 'John', 25, 50000, 1);
INSERT INTO employees (id, name, age, salary, department_id) VALUES (2, 'Jane', 30, 60000, 1);
INSERT INTO employees (id, name, age, salary, department_id) VALUES (3, 'Bob', 35, 70000, 2);
```

This inserts data into the "departments" and "employees" tables. The first two `INSERT INTO` statements add data to the "departments" table, and the last three statements add data to the "employees" table.

To retrieve data from the tables, you can use the `SELECT` statement:

```
SELECT * FROM departments;
```

This retrieves all the data from the "departments" table.

```
SELECT * FROM employees WHERE department_id = 1;
```

This retrieves all the data from the "employees" table where the "department_id" is equal to 1.

**One-to-One Relationship:**

A one-to-one relationship is a relationship between two tables where each row in one table is related to at most one row in the other table. One-to-one relationships are less common than one-to-many relationships, but they are still useful in certain scenarios.

In the context of the employees and departments tables, a one-to-one relationship might exist between an employee and their manager. Each employee has exactly one manager, and each manager is responsible for exactly one employee. To represent this relationship in the database, we could add a "manager_id" column to the employees table that references the id column of the employees table. The "manager_id" column would be a foreign key, indicating that it references the primary key of the employees table.

Here's what the SQL code to create the tables might look like:

```
CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    salary DECIMAL(10,2),
    department_id INT,
    manager_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id),
    FOREIGN KEY (manager_id) REFERENCES employees(id)
);
```

In this code, we've added a "manager_id" column to the employees table, and we've created a foreign key constraint that references the id column of the employees table. This establishes a one-to-one relationship between employees and their managers.

Here's an example of how you might use this schema to store data:

```
INSERT INTO departments (id, name) VALUES (1, 'Sales');
INSERT INTO departments (id, name) VALUES (2, 'Marketing');

INSERT INTO employees (id, name, age, salary, department_id, manager_id) VALUES (1, 'John', 25, 50000, 1, 2);
INSERT INTO employees (id, name, age, salary, department_id, manager_id) VALUES (2, 'Jane', 30, 60000, 1, 1);
```

In this example, we've added two employees to the database. John is an employee in the Sales department, and his manager is Jane. Jane is also an employee in the Sales department, and her manager is John. This represents a one-to-one relationship between each employee and their manager.

**Many-to-Many Relationship:**

A many-to-many relationship is a type of relationship between two tables where each row in the first table can be related to many rows in the second table, and each row in the second table can be related to many rows in the first table. In other words, there is no limit to the number of relationships that can exist between the two tables.

In the context of the employees and projects example, a many-to-many relationship might exist between employees and projects. Each employee can work on many projects, and each project can have many employees working on it. To represent this relationship in the database, we need a third table that connects the employees and projects tables. This is called a junction or intersection table, and it contains foreign keys to both the employees and projects tables.

Here's what the SQL code to create the tables might look like:

```
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    salary DECIMAL(10,2)
);

CREATE TABLE projects (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    description TEXT
);

CREATE TABLE employee_projects (
    employee_id INT,
    project_id INT,
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES employees(id),
    FOREIGN KEY (project_id) REFERENCES projects(id)
);
```

In this code, we've added a new table called employee_projects that has foreign keys to both the employees and projects tables. The primary key of the employee_projects table is a combination of the employee_id and project_id columns, which ensures that each relationship between an employee and a project is unique.

Here's an example of how you might use this schema to store data:

```
INSERT INTO employees (id, name, age, salary) VALUES (1, 'John', 25, 50000);
INSERT INTO employees (id, name, age, salary) VALUES (2, 'Jane', 30, 60000);

INSERT INTO projects (id, name, description) VALUES (1, 'Website Redesign', 'Redesigning company website');
INSERT INTO projects (id, name, description) VALUES (2, 'Mobile App Development', 'Developing a mobile app for iOS and Android');

INSERT INTO employee_projects (employee_id, project_id) VALUES (1, 1);
INSERT INTO employee_projects (employee_id, project_id) VALUES (1, 2);
INSERT INTO employee_projects (employee_id, project_id) VALUES (2, 1);
```

In this example, we've added two employees and two projects to the database. We've then used the employee_projects table to establish the relationships between employees and projects. John is working on both the Website Redesign and Mobile App Development projects, while Jane is working only on the Website Redesign project.
