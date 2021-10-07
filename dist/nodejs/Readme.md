# BusinessEmailValidator Wrapper for NodeJs

This is a business Email Validatore that checks if a sender is using a valid email or not.

example code:

```js
import isValidMail from "businessEmailValidator/businessEmailValidator.js";
console.log(isValidMail("xyz@custombusinessmail.com")); // true
console.log(isValidMail("xyz@gmail.com")); // false
console.log(isValidMail("xyz@email.com")); // false
console.log(isValidMail("xyz@emailproxsy.com")); // false
console.log(isValidMail("xyz@fakeinbox.com")); // false
```
