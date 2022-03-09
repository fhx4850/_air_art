from .MyBaseException import MyBaseException

class ObjectDoesNotExist(MyBaseException):
    """Exception output if object not found."""
    
    def __init__(self, errorMsg = None):
        super().set_default_msg('Does not exist')
        super().set_error_msg(errorMsg)