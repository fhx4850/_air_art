from services.ProfileService import ProfileService


class BaseServiceMixin(ProfileService):
    """Class mixin which contains all services."""
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__} = ({ProfileService.__name__})'