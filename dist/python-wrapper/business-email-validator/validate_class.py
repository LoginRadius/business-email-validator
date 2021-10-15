from future import __annotations__
from typing import Union, Optional
from .errors import *

import re

class ValidEmail:
    pass

class ValidBusinessEmail:
    pass

class ValidateBusinessMails:
    __slots__ = []
    
    def __init__(self, email: str) -> None:
        self.email = email
    
    def validate_email(email: str) -> Union[ValidEmail, bool]:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, email):
            return ValidEmail(email)
        else:
            return InvalidEmail(email)
