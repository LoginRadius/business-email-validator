# Ruby Wrapper Business Email Validator

## Usage

```rb
# Should return true
validTest = BusinessEmailValidator.validate("test@customdomai.com")
puts validTest.to_s # true

# Should return false
invalidTest = BusinessEmailValidator.validate("test@123.com")
puts invalidTest.to_s # false
```
