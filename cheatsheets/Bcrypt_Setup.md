bcrypt is a password-hashing library that is widely used for securing user passwords in web applications. It is designed to be computationally expensive and time-consuming to prevent brute-force attacks, dictionary attacks, and other types of password cracking attempts.

When using bcrypt with an Express server, you typically need to perform the following steps:

1. Install the bcrypt library using npm. You can do this by running the following command in your project directory:

   ```
   npm install bcrypt
   ```

2. Import the bcrypt library in your server.js or app.js file:

   ```javascript
   const bcrypt = require('bcrypt');
   ```

3. Use the bcrypt.hash() method to generate a hashed password from the user's plaintext password. The hash() method takes two arguments: the plaintext password and the salt rounds. The salt rounds specify the number of rounds of hashing that should be performed, which affects the strength of the resulting hash. A common value for salt rounds is 10. Please keep in mind that you should not put a really high number for the salt value, as your processor will likely be unable to handle it and you could overwork your machine.

   ```javascript
   const plaintextPassword = 'mypassword';
   const saltRounds = 10;

   bcrypt.hash(plaintextPassword, saltRounds, (err, hash) => {
     if (err) {
       console.error(err);
       return;
     }
     console.log('Hashed password:', hash);
   });
   ```

4. Store the hashed password in your database, instead of the plaintext password.

5. When a user logs in, use the bcrypt.compare() method to compare the plaintext password entered by the user with the stored hashed password. The compare() method takes two arguments: the plaintext password and the hashed password.

   ```javascript
   const userEnteredPassword = 'mypassword';
   const storedHashedPassword = '...'; // this is the password that is stored in the database

   bcrypt.compare(userEnteredPassword, storedHashedPassword, (err, result) => {
     if (err) {
       console.error(err);
       return;
     }
     if (result) {
       console.log('Passwords match!');
     } else {
       console.log('Passwords do not match.');
     }
   });
   ```

By using bcrypt to hash and store passwords securely, you can help protect your users' accounts and personal information from unauthorized access and data breaches.