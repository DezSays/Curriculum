# Guide to pg-promise with Express

## Introduction

This beginner's guide will walk you through setting up a basic Express server with pg-promise for connecting to a PostgreSQL database. Before you begin, make sure you have Node.js installed on your machine. Additionally, have PostgreSQL installed, and consider using a tool like [ElephantSQL](https://www.elephantsql.com/) for cloud-based PostgreSQL services.

## Step 1: Initialize Your Project

Open your terminal and create a new folder for your project:

```bash
mkdir express-pg-promise-guide
cd express-pg-promise-guide
npm init -y
```

## Step 2: Install Express and pg-promise

Install Express and pg-promise using npm:

```bash
npm install express pg-promise
```

## Step 3: Set Up Your Express Server

Create a file named `server.js` in your project folder and open it in your preferred code editor. Copy and paste the following code into `server.js`:

```javascript
// server.js
const express = require('express');
const pg = require('pg-promise')();
const app = express();

// Database connection
const db = pg("postgres://your_username@localhost:5432/your_database");

app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000');
});

// Insert data
app.get('/insert', (req, res) => {
  db.none('INSERT INTO users(name, age) VALUES($1, $2)', ['John Doe', 25])
    .then(() => {
      res.send('Data inserted successfully.');
    })
    .catch(error => {
      console.error('Error inserting data:', error);
      res.status(500).send('Error inserting data.');
    });
});

// Select data
app.get('/select', (req, res) => {
  db.any('SELECT * FROM users')
    .then(data => {
      res.json(data);
    })
    .catch(error => {
      console.error('Error selecting data:', error);
      res.status(500).send('Error selecting data.');
    });
});

// Update data
app.get('/update', (req, res) => {
  db.none('UPDATE users SET age = $1 WHERE name = $2', [30, 'John Doe'])
    .then(() => {
      res.send('Data updated successfully.');
    })
    .catch(error => {
      console.error('Error updating data:', error);
      res.status(500).send('Error updating data.');
    });
});

// Delete data
app.get('/delete', (req, res) => {
  db.none('DELETE FROM users WHERE name = $1', ['John Doe'])
    .then(() => {
      res.send('Data deleted successfully.');
    })
    .catch(error => {
      console.error('Error deleting data:', error);
      res.status(500).send('Error deleting data.');
    });
});
```

Replace `your_username` and `your_database` in the database connection string with your PostgreSQL credentials and database name.

## Step 4: Run Your Express Server

Run your Express server with the following command:

```bash
node server.js
```

Visit the following URLs in your browser or a tool like [Postman](https://www.postman.com/) to test the database operations:

- [http://localhost:3000/insert](http://localhost:3000/insert)
- [http://localhost:3000/select](http://localhost:3000/select)
- [http://localhost:3000/update](http://localhost:3000/update)
- [http://localhost:3000/delete](http://localhost:3000/delete)

Congratulations! You've successfully set up a basic Express server with pg-promise, connected to a PostgreSQL database, and performed basic database operations. Explore more features and best practices in the [pg-promise documentation](https://vitaly-t.github.io/pg-promise/index.html) and [Express documentation](https://expressjs.com/).