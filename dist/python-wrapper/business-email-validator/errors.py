from future import __annotations__

class InvalidBusinessMail:
    '''
    This will be raised when a email is not a valid business email
    '''
    def __init__(self, email) -> None:
        self.email = email
    
    def __str__(self) -> str:
        return f'<Invalid business email | {self.email} is not a valid business email>'

class InvalidEmail: 
    '''
    This will be raised when a email is not a valid email
    '''
    def __init__(self, email) -> None:
        self.email = email
    
    def __str__(self):
        return f'<Invalid email | {self.email} is not a valid email>'
