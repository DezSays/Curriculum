# Top PSQL Commands for Beginners

Welcome to the world of PostgreSQL! If you're just starting with `psql`, these essential commands will help you navigate and interact with databases. Let's get started:

1. **Exit psql:**
   ```plaintext
   \q
   ```
   - **When to Use:** To exit the psql command-line interface.

2. **List all databases:**
   ```plaintext
   \l
   ```
   - **When to Use:** To display a list of all available databases on the server.

3. **Connect to a database:**
   ```plaintext
   \c <database>
   ```
   - **When to Use:** To connect to a specific database.

4. **List all tables in the current database:**
   ```plaintext
   \dt
   ```
   - **When to Use:** To view a list of tables within the currently connected database.

5. **Describe the specified table:**
   ```plaintext
   \d <table>
   ```
   - **When to Use:** To view details about the structure of a specific table.

6. **Retrieve all data from a table:**
   ```sql
   SELECT * FROM <table>;
   ```
   - **When to Use:** To fetch all columns and rows from a specific table.

7. **Insert a new row into a table:**
   ```sql
   INSERT INTO <table> (<columns>) VALUES (<values>);
   ```
   - **When to Use:** To add a new record (row) to a table.

8. **Update data in a table:**
   ```sql
   UPDATE <table> SET <column> = <value> WHERE <condition>;
   ```
   - **When to Use:** To modify existing data in a table based on specified conditions.

9. **Delete data from a table:**
   ```sql
   DELETE FROM <table> WHERE <condition>;
   ```
   - **When to Use:** To remove records from a table based on specified conditions.

10. **Execute SQL commands from a file:**
    ```plaintext
    \i <file>
    ```
    - **When to Use:** To run SQL commands stored in an external file.

11. **Connect as the postgres user:**
    ```plaintext
    psql -U postgres
    ```
    - **When to Use:** To connect to the psql command-line interface as the postgres user.

12. **Add a new column to a table:**
    ```sql
    ALTER TABLE <table> ADD COLUMN <column_definition>;
    ```
    - **When to Use:** To modify the structure of a table by adding a new column.

13. **Delete a table:**
    ```sql
    DROP TABLE <table>;
    ```
    - **When to Use:** To remove a table and its data from the database.

14. **Create a new database:**
    ```sql
    CREATE DATABASE <name>;
    ```
    - **When to Use:** To create a new database for storing tables and data.

15. **Get help on SQL commands:**
    ```plaintext
    \h
    ```
    - **When to Use:** To get help on SQL commands and syntax.