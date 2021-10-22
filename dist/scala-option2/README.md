## About
  This is the wrapper for business-email-validator in Scala

## Steps to Run the program
This is a utility class to validate email address in a provided file.

1. Include the following dependencies in your gradle file.

	libraryDependencies ++= Seq("com.lihaoyi" %% "upickle" % "0.9.5","com.lihaoyi" %% "os-lib" % "0.7.8")  

2. Include this class in your scala project.
3. Change the file path that includes email providers, it is commented in the file itself.
4. Call the validator using as shown, it will return if the provided email is business email or not.

	val validator = new BusinessEmailValidator();
        validator.validator("abc@dot.com");
    
## Author Details
  [Kumar Aggarwal](https://github.com/kaggrwal) on 17th October, 2021.

