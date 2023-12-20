# JavaScript If/Else Statements and Ternary Operators Cheatsheet

## If/Else Statements

### Basic If Statement

```javascript
if (condition) {
  // Code to execute if the condition is true
}
```

### If/Else Statement

```javascript
if (condition) {
  // Code to execute if the condition is true
} else {
  // Code to execute if the condition is false
}
```

### If/Else If/Else Statement

```javascript
if (condition1) {
  // Code to execute if condition1 is true
} else if (condition2) {
  // Code to execute if condition2 is true
} else {
  // Code to execute if none of the conditions are true
}
```

### Nested If/Else Statement

```javascript
if (condition1) {
  if (condition2) {
    // Code to execute if both condition1 and condition2 are true
  } else {
    // Code to execute if only condition1 is true
  }
} else {
  // Code to execute if condition1 is false
}
```

## Ternary Operators

### Basic Ternary Operator

```javascript
let result = (condition) ? trueValue : falseValue;
```

### Nested Ternary Operator

```javascript
let result = (condition1) ? (nestedCondition1 ? value1 : value2) : (condition3 ? value3 : value4);
```

### Ternary Operator in Return Statement

```javascript
function exampleFunction(parameter) {
  return (parameter === 42) ? "Answer to the Ultimate Question of Life, the Universe, and Everything" : "Not the answer";
}
```

### Using Ternary Operator for Assignment

```javascript
let status = (isOnline) ? "Online" : "Offline";
```

## Notes:

- If/else statements are used for conditional execution of code blocks based on the evaluation of a condition.

- Ternary operators provide a concise way to write conditional expressions in a single line.

- Ternary operators are often used for simple conditions, while if/else statements are more suitable for complex conditions or multiple branches.

- Keep code readability in mind; choose between if/else statements and ternary operators based on the context and complexity of the condition.