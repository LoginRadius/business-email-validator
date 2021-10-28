# Business Email Validator for JuliaLang

This is a business email validator that checks the email given.
In order to run it, you need to have the JSON package installed.

And then, you just need to include it:
```julia
include("business_email_validator.jl")

println(validate("hello@gmail.com")) # true
println(validate("@hello@gmail.com")) # true
println(validate("hello@hello")) # false
```
