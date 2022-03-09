from .WrongDataReceived import WrongDataReceived
from .ObjectDoesNotExist import ObjectDoesNotExist
from .CreationError import CreationError
from .UpdateError import UpdateError
import functools

class BaseExceptionsMixin(WrongDataReceived):
    """General view of all exceptions."""
    
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__} = ({WrongDataReceived.__name__})'
    
    
    @staticmethod
    def baseException(exceptClass, msg = None):
        """Generic decorator for exception handling."""
        def func(foo):
            @functools.wraps(foo)
            def wrapper(*args, **kwargs):
                try:
                   foo()
                except:
                    if msg:
                        raise exceptClass(msg)
                    else:
                        raise exceptClass
            return wrapper 
        return func
    
    @staticmethod
    def getWrongDataReceived():
        return WrongDataReceived
    
    @staticmethod
    def getObjectDoesNotExist():
        return ObjectDoesNotExist
    
    @staticmethod
    def getCreationError():
        return CreationError
    
    @staticmethod
    def getUpdateError():
        return UpdateError