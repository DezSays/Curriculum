# Guide: Connecting an HTML File from the Frontend to an Express Route on the Backend

## Step 1: Initialize Your Project

Open your terminal and create the project structure:

```bash
mkdir Full_Stack_Connection_Example
cd Full_Stack_Connection_Example
mkdir client
mkdir server
```

## Step 2: Set Up the Server Package

Navigate to the "server" folder and initialize the Node.js project with a package.json file:

```bash
cd server
npm init -y
```

## Step 3: Install Express

Install Express in the "server" folder:

```bash
npm install express
```

## Step 4: Create HTML File

Create an "html" folder in the "client" folder and add a file named "login.html". This file will serve as your login page. Add the following content:

```html
<!-- client/html/login.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login Page</title>
</head>
<body>
  <h1>Login Page</h1>
  <p>Welcome to the login page!</p>
</body>
</html>
```

## Step 5: Set Up Your Express Server

Create a file named "server.js" in the "server" folder and open it in your preferred code editor. Copy and paste the following code into "server.js":

```javascript
// server/server.js
const express = require('express');
const path = require('path');
const app = express();

app.get('/login', (req, res) => {
  // Resolve the path to the login.html file
  const loginPage = path.resolve(__dirname, '..', 'client', 'html', 'login.html');
  
  // Render the login.html file
  res.sendFile(loginPage);
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

In this code, we use `path.resolve(__dirname, '..', 'client', 'html', 'login.html')` to navigate from the "server" folder to the "client/html" folder.

## Step 6: Run Your Express Server

Run your Express server from the "server" folder:

```bash
node server.js
```

Visit [http://localhost:3000/login](http://localhost:3000/login) in your web browser to see the rendered login page.

Congratulations! You've successfully set up a basic Express server with a login endpoint that renders an HTML page, following the specified file structure with the `package.json` file inside the "server" folder. Feel free to customize the HTML page and explore more features in the [Express documentation](https://expressjs.com/). 