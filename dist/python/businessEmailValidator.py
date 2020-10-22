# Author : Divya Gupta
# Github Profile : https://github.com/divya144


import json
import os
import sys

# Function to check if domain name exists or not
def if_exist(email,email_list):
    for i in email_list:
        if(i==email):
            return True
    return False

# Function to save all domain names in a list
def open_file():
    fileDir = os.path.abspath('../..')
    filename = os.path.join(fileDir,'src/freeEmailService.json')
    print(filename)
    file1=open(filename,"r")
    email_list = json.load(file1)
    return email_list

# Function to validate email
def validate(email):
    email_list = open_file()
    pos = email.find('@')
    if(pos>0 and pos<len(email)-3):
        email_domain = email[pos+1 : ]
        if(if_exist(email_domain,email_list)==True):
            return True
    return False

if __name__ == "__main__":
    validate(sys.argv[1])
