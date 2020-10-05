using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Mail;
using Newtonsoft.Json;

namespace BusinessEmailValidator
{
    public class EmailValidator
    {
        /// <summary>
        /// Load list of free email domains from the json file
        /// </summary>
        public static Dictionary<string, bool> LoadJson()
        {
            Dictionary<string, bool> domainListItems = null;
            using (StreamReader r = new StreamReader(@"src\freeEmailService.json"))
            {
                string json = r.ReadToEnd();
                domainListItems = JsonConvert.DeserializeObject<Dictionary<string,bool>>(json);
            }
            return domainListItems;
        }

        /// <summary>
        /// Check for the free email domain from the emailId
        /// </summary>
        /// <param name="emailId">EmailId of the user</param>
        /// <param name="error">Error from the method</param>
        
        public static bool CheckFreeEmailDomain(string emailId,out string error)
        {
            error = "Not a free email domain";
            try
            {
                //Check for a valid email address
                var emailDomain = new MailAddress(emailId).Host;
                //Load FreeEmailDomain list
                var domainList = LoadJson();
                foreach (var domain in domainList)
                {
                    //Check for free email domain
                    if (emailDomain == domain.Key)
                    {
                        error = "Free email domain";
                        return true;
                    }
                }
            }
            catch (FormatException)
            {
                error = "Not a valid email address";
                return false;
            }
            return false;
        }
    }
}
