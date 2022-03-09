from .MyBaseException import MyBaseException


class WrongDataReceived(MyBaseException):
    """Exception for bad data."""
    
    def __init__(self, errorMsg = None):
        super().set_default_msg('Error while updating')
        super().set_error_msg(errorMsg)