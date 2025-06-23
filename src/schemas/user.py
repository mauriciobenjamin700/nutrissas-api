from datetime import datetime
from pydantic import EmailStr

from src.core import BaseSchema
from src.core.enums import UserGender

class BaseUserSchema(BaseSchema):
    """
    BaseUserSchema is a Pydantic model that serves as a base class for user-related schemas.

    Attributes:
        name (str): The name of the user.
        gender (UserGender): The gender of the user, represented as an enum.
        birth_date (datetime): The birth date of the user.
        state (str): The state where the user resides.
        city (str): The city where the user resides.
        cep (str): The postal code of the user's address.
        complement (str | None): Additional address information, optional.
        email (EmailStr): The email address of the user.
    """
    name: str
    gender: UserGender
    birth_date: datetime
    state: str
    city: str
    cep: str
    complement: str | None = None
    email: EmailStr

class UserRequest(BaseUserSchema):
    """
    UserRequest is a Pydantic model that represents the data required to create or update a user.

    Attributes:
        name (str): The name of the user.
        gender (UserGender): The gender of the user, represented as an enum.
        birth_date (datetime): The birth date of the user.
        state (str): The state where the user resides.
        city (str): The city where the user resides.
        cep (str): The postal code of the user's address.
        complement (str | None): Additional address information, optional.
        email (EmailStr): The email address of the user.
        password (str): The password for the user account.
        have_illness (bool): Indicates whether the user has an illness.
        illness (str | None): The type of illness the user has, if any.
        illness_description (str | None): A description of the user's illness, if applicable.
    """
    password: str
    have_illness: bool = False
    illness: str | None = None
    illness_description: str | None = None
