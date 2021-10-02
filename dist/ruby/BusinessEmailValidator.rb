# Author : Sashank Agarwal
# Github Profile : https://github.com/sasagarw

require "json"

# if_exists checks if domain name exists or not
def if_exist(domain, email_list)
    email_list.each_key do |key|
        if key == domain
            return true
        end
    end
    return false
end

# open_file saves all domain names in a list from a file present at 'business-email-validator/src/freeEmailService.json'
def open_file()
    filename = "./src/freeEmailService.json"
    file = File.open filename
    email_list = JSON.load file
    return email_list
end

# validate validates the email passed as argument
def validate(email)
    email_list = open_file
    pos = email.index('@')
    if pos > 0 and pos < email.length - 3
        email_domain = email[pos+1..]
        if if_exist email_domain, email_list
            return true
        end
    end
    return false
end
