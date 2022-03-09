class MyBaseException(Exception):
    """The base representation of the exception for inheritance."""
    
    def __init__(self, errorMsg = None):
        self.errorMsg = errorMsg
        self.defaultMsg = None
        
    def __str__(self):
        if self.errorMsg:
            return '===> ' + self.errorMsg
        else:
            return '===> ' + self.defaultMsg
        
        
    def set_default_msg(self, msg):
        self.defaultMsg = msg
        
    def set_error_msg(self, msg = None):
        self.errorMsg = msg