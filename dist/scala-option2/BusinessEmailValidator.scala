
//add the following dependencies
/*
libraryDependencies ++= Seq(
  "com.lihaoyi" %% "upickle" % "0.9.5",
 "com.lihaoyi" %% "os-lib" % "0.7.8")
 */

import scala.collection.mutable.LinkedHashMap


class BusinessEmailValidator() {


   def validator(email: String): Boolean = {

      println("Validating for email: " + email)
      val index = email.lastIndexOf("@")

      if (index == -1) return false

      val domain: String = email.substring(index + 1)


      val freeEmailProviders: LinkedHashMap[String, String] = getProviders(): LinkedHashMap[String, String]

      if(freeEmailProviders.contains(domain)){
         return false;
      }
      return true;
   }

   def getProviders(): LinkedHashMap[String,String] ={
            val freeEmailProviders = os.read(os.pwd/"src"/"main"/"scala"/"freeEmailService.json") //change the path to actual location of json file
            val data = ujson.read(freeEmailProviders)
            return data.value.asInstanceOf[LinkedHashMap[String,String]]
   }
}


// Demo code to run the validator
/*
object Demo {
   def main(args: Array[String]) {
      val validator = new BusinessEmailValidator();

      print(validator.validator("abc@dot.com"));
   }
}*/
