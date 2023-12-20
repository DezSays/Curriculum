**Selecting Elements and Appending Content**

Instructions:
1. Create a new HTML file and save it with a .html extension, for example, "index.html".
2. Inside the HTML file, create a `<div>` element and give it an ID of "myDiv".
3. Create three `<p>` tags and write down your favorite foods within each tag.
4. Create two additional `<p>` tags and give them a class called "myClass". In the first `<p>` tag, write your first name, and in the second `<p>` tag, write your last name.
5. Create a `<button>` element and give it an ID of "newBtn". Set the inner text of the button as "Click".
6. Create a new JavaScript file and save it with a .js extension, for example, "script.js".
7. Link the JavaScript file to the HTML file by adding the following line of code within the `<head>` section of the HTML file:
   ```html
   <script src="script.js"></script>
   ```
8. Open the JavaScript file you created in a text editor.

Exercise:
Your task is to write JavaScript code that accomplishes the following steps:

1. Select the element with the ID "myDiv" and store it in a variable called `myDiv`.
2. Select all `<p>` elements on the page and store them in a variable called `paragraphs`.
3. Select all elements with the class "myClass" and store them in a variable called `myElements`.
4. Select the button element with the ID "newBtn" and store it in a variable called `newButton`.
5. Add an event listener to the `newButton` variable, listening for a "click" event.
6. Inside the event listener function, create a new `<p>` element using the `createElement` method and set its inner text to "Hello World".
7. Append the newly created `<p>` element as a child to the `myDiv` element using the `appendChild` method.

Remember to use appropriate DOM methods and event handling techniques to achieve these tasks.

Once you have completed the exercise, save both the HTML and JavaScript files. Then, open the HTML file in a web browser to see the results. You can right-click on the HTML file and choose "Open with" to select your preferred browser.

Good luck with the exercise! Practice selecting elements using the DOM, adding event listeners, and dynamically modifying the content of the web page. Enjoy exploring and enhancing the functionality of your web page!