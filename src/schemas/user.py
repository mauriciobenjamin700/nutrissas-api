from datetime import datetime
from pydantic import EmailStr, Field

from src.core import BaseSchema
from src.core.enums import UserGender

class BaseUserSchema(BaseSchema):
    """
    BaseUserSchema is a Pydantic model that serves as a base class for user-related schemas.

    Attributes:
        name (str): The name of the user.
        email (EmailStr): The email address of the user.
    """
    name: str
    email: EmailStr

class UserCreate(BaseUserSchema):
    """
    UserRequest is a Pydantic model that represents the data required to create a user.

    Attributes:
        name (str): The name of the user.
        email (EmailStr): The email address of the user.
        password (str): The password for the user account.
    """
    password: str


class UserLogin(BaseSchema):
    """
    UserLogin is a Pydantic model that represents the data required for user authentication.

    Attributes:
        email (EmailStr): The email address of the user.
        password (str): The password for the user account.
    """
    email: EmailStr
    password: str


class UserResponse(BaseUserSchema):
    """
    UserResponse is a Pydantic model that represents the response data for a user.

    Attributes:
        id (int): The unique identifier of the user.
        name (str): The name of the user.
        email (EmailStr): The email address of the user.
        birth_date (datetime | None): The birth date of the user in ISO format.
        state (str | None): The state where the user resides, represented as a two-character code.
        city (str | None): The city where the user resides.
        cep (str | None): The postal code (CEP) of the user's address.
        complement (str | None): Additional address information, if any.
        created_at (datetime): Timestamp when the user record was created.
        updated_at (datetime): Timestamp when the user record was last updated.
    """
    id: str = Field(description="Unique identifier of the user")
    gender: UserGender | None = Field(
        None, 
        description="User Gender", 
        examples=[UserGender.MALE]
    )
    birth_date: datetime | None = Field(
        None, 
        description="User Birth Date in ISO format",
        examples=["1990-01-01T00:00:00"]
    )
    state: str | None = Field(
        None, 
        description="User State represented as a two-character code",
        examples=["SP"]
    )
    city: str | None = Field(
        None,
        description="User City",
        examples=["São Paulo"]
    )
    cep: str | None = Field(
        None, 
        description="User Postal Code (CEP)",
        examples=["01000-000"]
    )
    complement: str | None = Field(
        None, 
        description="Additional address information, if any",
        examples=["Apt 123"]
    )
    created_at: datetime = Field(
        description="Timestamp when the user record was created",
        examples=["2023-10-01T12:00:00Z"]
    )
    updated_at: datetime = Field(
        description="Timestamp when the user record was last updated",
        examples=["2023-10-01T12:00:00Z"]
    )


class TokenData(BaseSchema):
    """
    TokenData is a Pydantic model that represents the data contained in a JWT token.

    Attributes:
        sub (str): The subject of the token, typically the user ID.
    """
    sub: str


class TokenResponse(BaseSchema):
    """
    TokenResponse is a Pydantic model that represents the response data for a JWT token.

    Attributes:
        access_token (str): The JWT access token.
        token_type (str): The type of the token, typically "bearer".
    """
    access_token: str
    token_type: str = "bearer"
    user: UserResponse
