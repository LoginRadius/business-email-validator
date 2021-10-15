# Python `business-email-validator`

Everthing is to done and accessed to the class `ValidateBusinessMails`. And it has to be imported like this:
```python
from business_email_validator import ValidateBusinessMails
```

This class provides 3 properties and 2 independent functions
- Properties: `email`, `email_verifier`, `business_email_verifier`
- Independent Functions: `validate_email`, `validate_business_email`

Usage:
- validate_email `(Independent Function)`:
 ```python
from business_email_validator import ValidateBusinessMails, ValidEmail
try:
  email_validation = ValidateBusinessMails.validate_email(examplemail@domain.com)
except ValidEmail:
  pass
```
- validate_business_email `(Independent Function)`:
 ```python
from business_email_validator import ValidateBusinessMails, ValidEmail, ValidBusinessEmail
try:
  email_validation = ValidateBusinessMails.validate_business_email(examplemail@domain.com)
except ValidEmail or ValidBusinessEmail:
  pass
```

- email_verifier `(Property)`:
  
  Prints `True` when it is a `valid email`.
```python
print(ValidateBusinessMails(examplemail@domain.com).email_verifier)
```
- business_email_verifier `(Property)`:
  
  Prints `True` when it is a `valid business email`.
```python
print(ValidateBusinessMails(examplemail@domain.com).business_email_verifier)
```
