import isValidMail from "./businessEmailValidator.js";

console.log(isValidMail('xyz@custombusinessmail.com')); // true
console.log(isValidMail('xyz@gmail.com')); // false
console.log(isValidMail('xyz@email.com')); // false
console.log(isValidMail('xyz@emailproxsy.com')); // false
console.log(isValidMail('xyz@fakeinbox.com')); // false

