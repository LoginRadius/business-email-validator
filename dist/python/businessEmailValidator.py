# Author : Divya Gupta
# update : Tirtharaj Sinha (https://github.com/tirtharajsinha)
# Github Profile : https://github.com/divya144


import json
import os
import sys
import re

# Function to check if domain name exists or not
def if_exist(email, email_list):
    if(email in email_list):
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
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        email_domain = email[pos+1:]
        if(if_exist(email_domain, email_list.keys()) == True):
            return True
    return False


# validate a list of email and return in dict
def validate_list(entry_list=[]):
    email_dict = {}
    for entry in entry_list:
        try:
            email_dict[entry] = validate(entry)
        except:
            email_dict[entry] = False
    return email_dict
