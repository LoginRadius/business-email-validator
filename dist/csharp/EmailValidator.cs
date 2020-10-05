using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Mail;
using Newtonsoft.Json;

namespace BusinessEmailValidator
{
    public class EmailValidator
    {
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

        public static bool CheckFreeEmailDomain(string emailId)
        {
            try
            {
                var emailDomain = new MailAddress(emailId).Host;
                var domainList = LoadJson();
                foreach (var domain in domainList)
                {
                    if (emailDomain == domain.Key)
                        return true;
                }
            }
            catch (FormatException)
            {
                return false;
            }
            return false;
        }
    }
}
