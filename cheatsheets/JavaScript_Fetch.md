# Using Fetch in Vanilla JavaScript

## Introduction

In web development, when we want to get data from a server or send data to a server, we use a process called making HTTP requests. The `fetch` function in JavaScript is a tool that helps us do this. This readme will guide you through using `fetch` in simple terms, explaining each step for beginners.

## Basic Fetch Request

Let's start with a simple example of getting data from a server using `fetch`:

```javascript
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

Here's what each part does:

- `fetch('https://jsonplaceholder.typicode.com/todos/1')`: This tells the browser to go and get data from the URL provided.
  
- `.then(response => response.json())`: Once the data is received, this part says, "Okay, take the response and convert it to JSON format so we can use it like a JavaScript object."

- `.then(data => console.log(data))`: Now that we have the data as a JavaScript object, let's print it to the console.

- `.catch(error => console.error('Error:', error));`: If something goes wrong (like the server is down or the URL is wrong), this part catches the error and tells us there's a problem.

In simpler terms, it's like asking someone for information, understanding the response, and then doing something with that information.

## Sending Data with POST

Now, let's see how we can send data to a server, like when you submit a form on a website:

```javascript
const postData = {
  title: 'My awesome post',
  body: 'This is the content of my post.',
  userId: 1,
};

fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(postData),
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

Here's a breakdown:

- `const postData = { ... };`: This is just creating an object with some data.

- `fetch('https://jsonplaceholder.typicode.com/posts', { ... });`: This is telling the server, "I want to send you some data using the POST method."

- `headers: { 'Content-Type': 'application/json' }`: This part says, "The data I'm sending is in JSON format."

- `body: JSON.stringify(postData)`: Here, we're turning our JavaScript object into a string so the server can understand it.

So, it's like filling out a form online, hitting the submit button, and getting a response.