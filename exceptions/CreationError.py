from .MyBaseException import MyBaseException


class CreationError(MyBaseException):
    """Throw an error on creation."""
    def __init__(self, errorMsg = None):
        super().set_default_msg('Error while creating')
        super().set_error_msg(errorMsg)