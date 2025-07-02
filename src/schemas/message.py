from src.core import BaseSchema


class MessageResponse(BaseSchema):
    """
    MessageResponse is a schema for returning messages in API responses.

    Attributes:
        detail (str): The message to be returned.
    """
    
    detail: str