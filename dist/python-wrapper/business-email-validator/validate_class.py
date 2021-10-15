from future import __annotations__

import functools
import os
import re
from pathlib import Path
from typing import Optional, Union

from .classes import *


class ValidateBusinessMails:
    '''
        This class provides 3 properties and 2 independent functions
        - Properties: email, email_verifier, business_email_verifier
        - Independent Functions: validate_email, validate_business_email

        Usage:
        - validate_email:
            ValidateBusinessMails.validate_email(examplemail@domain.com)
        - validate_business_email:
            ValidateBusinessMails.validate_business_email(examplemail@domain.com)

        - email_verifier:
            ValidateBusinessMails(examplemail@domain.com).email_verifier
        - business_email_verifier:
            ValidateBusinessMails(examplemail@domain.com).business_email_verifier
    '''
    __slots__ = ['email', 'email_verifier', 'business_email_verifier']

    def __init__(self, email: str) -> None:
        self.email = email

    def __str__(self) -> str:
        return f'<Validate Business Mails | {self.email}>'

    @functools.lru_cache(maxsize=2)
    def validate_email(email: str) -> Optional[Union[ValidEmail, InvalidEmail]]:
        '''
            This is function which validate if is it a email or not.
            It raises `Union[ValidEmail, InvalidEmail]`
            The function is also cached using lru_cache
        '''
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, email):
            raise InvalidEmail(email)
        else:
            raise ValidEmail(email)

    @functools.lru_cache(maxsize=2)
    def validate_business_email(email: str) -> Optional[Union[ValidBusinessEmail, InvalidBusinessMail]]:
        '''
            This is function which validate if is it a business email or not.
            It raises `Union[ValidBusinessEmail, InvalidBusinessMail]`
            The function is also cached using lru_cache
        '''
        try:
            email_validation = validate_email(email)
        except ValidEmail:
            pass

        BASE_DIR = Path(__file__).resolve().parent.parent
        data_set_path = BASE_DIR / os.path.join('freeEmailService.txt')
        with open(data_set_path, 'r') as f:
            data_set = list(map(lambda domain: domain.strip(
                '\n').strip(' ').lower(), f.readlines()))
        if email.strip('\n').strip(' ').lower() in data_set:
            raise InvalidBusinessMail(email)
        else:
            raise ValidBusinessEmail(email)

    @property
    @functools.lru_cache(maxsize=2)
    def email_verifier(self) -> bool:
        '''
            This is function which validate if is it a email or not (property).
            It return `bool`
            The function is also cached using lru_cache
        '''
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, self.email):
            return False
        else:
            return True

    @property
    @functools.lru_cache(maxsize=2)
    def business_email_verifier(self) -> bool:
        '''
            This is function which validate if is it a business email or not (property).
            It return `bool`
            The function is also cached using lru_cache
        '''
        try:
            email_validation = validate_email(self.email)
        except ValidEmail:
            pass

        BASE_DIR = Path(__file__).resolve().parent.parent
        data_set_path = BASE_DIR / os.path.join('freeEmailService.txt')
        with open(data_set_path, 'r') as f:
            data_set = list(map(lambda domain: domain.strip(
                '\n').strip(' ').lower(), f.readlines()))
        if email.strip('\n').strip(' ').lower() in data_set:
            return False
        else:
            return True
