from datetime import datetime
from uuid import uuid4


def id_generator() -> str:
    """
    Generates a unique identifier for a user.

    Returns:
        str: A unique identifier in the form of a UUID string.
    """
    return str(uuid4())


def get_current_time() -> datetime:
    """
    Gets the current UTC time.

    Returns:
        datetime: The current UTC time.
    """
    return datetime.now().astimezone(datetime.timezone.utc)