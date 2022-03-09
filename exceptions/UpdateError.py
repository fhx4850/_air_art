from .MyBaseException import MyBaseException


class UpdateError(MyBaseException):
    """Exception while updating."""
    
    def __init__(self, errorMsg = None):
        super().set_default_msg('Error while updating')
        super().set_error_msg(errorMsg)
