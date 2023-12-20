# Step-by-Step Guide: Creating an Express Server

Creating an Express server is a fundamental skill for web developers. Express is a fast, unopinionated, minimalist web framework for Node.js, making it easy to build robust and scalable web applications. This step-by-step guide will walk you through creating a simple Express server with examples.

## Prerequisites

Before you start, make sure you have Node.js and npm installed on your machine. You can download them from [Node.js official website](https://nodejs.org/).

## Step 1: Initialize Your Project

1. Open your terminal and create a new folder for your project.

   ```bash
   mkdir express-server-example
   ```

2. Navigate into the project folder.

   ```bash
   cd express-server-example
   ```

3. Initialize a new Node.js project.

   ```bash
   npm init -y
   ```

## Step 2: Install Express

1. Install Express using npm.

   ```bash
   npm install express
   ```

2. This will add Express as a dependency in your `package.json` file.

## Step 3: Create Your Express Server

1. Create a file named `server.js` in your project folder.

   ```bash
   touch server.js
   ```

2. Open `server.js` in your preferred code editor.

3. Import Express and create an instance of the app.

   ```javascript
   // server.js
   const express = require('express');
   const app = express();
   ```

4. Define a route to handle incoming requests.

   ```javascript
   app.get('/heartbeat', (req, res) => {
     res.send('Heartbeat steady!');
   });
   ```

5. Set the server to listen on a specific port.

   ```javascript
   const PORT = 3000;

   app.listen(PORT, () => {
     console.log(`Server is running on http://localhost:${PORT}`);
   });
   ```

## Step 4: Run Your Express Server

1. In your terminal, run the following command:

   ```bash
   node server.js
   ```

2. Open your web browser and go to `http://localhost:3000/heartbeat`. You should see the message "Heartbeat steady!"

Congratulations! You've successfully created a simple Express server named `server.js` that responds to a GET request on the `/heartbeat` route. This is a basic example, and from here, you can explore more features and complexities of Express as you build your web applications. 