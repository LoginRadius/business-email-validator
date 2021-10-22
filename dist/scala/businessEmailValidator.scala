import scala.io.Source
import scala.collection.mutable.ListBuffer
import scala.util.control.Breaks._ 

object BusinessEmailValidator 
{  
   	def main(args: Array[String]) 
	{  
		breakable 
		{
			//validating the arguments
			if(args.size != 1)
			{
				println("Invalid Arguments")
				break
			}

			//further validating the business email address
			if(validate_email(args(0)) == false)
			{
				println("Invalid Business Email Address")
				break
			}
			println("Valid Business Email Address")
		}
    }  

	//validates business email address after performing multiple tests
    def validate_email(email:String) : Boolean =
	{ 
		//finding the position of '@' and testing its validity
        var symbol_pos = email.indexOf('@')
		
        if(symbol_pos!=0 && symbol_pos!=(email.length()-1))
		{
			//split the email address using sybmol '@' and save second part in domain
			var domain = email.split('@')(1)
			if(is_freeEmailService(domain) == false)
				return true
			else
				return false
		}
		else
			return false
    }

	def is_freeEmailService(domain:String) : Boolean =
	{
		//import free email services as a list from json file
		var fileDir = "../../src/"
		var filename = "freeEmailService.json"
		
		var freeEmailService = ListBuffer[String]()
		
		for(line<-Source.fromFile(fileDir+filename).getLines){
			var domainName = line.split(':')(0).trim()
			//omit the first and last line of the json file and store the remaining free domain names without ""
			if(domainName.equals("{") == false && domainName.equals("}") == false)
				freeEmailService+= domainName.substring(1, domainName.length()-1);
		}

		//checking if domain of given email address is a free email service
		if(freeEmailService.contains(domain) == true)
		{
			return true	
		}
		else
			return false
	}
} 