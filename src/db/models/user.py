from datetime import datetime
from sqlalchemy import String, Text, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column


from src.core import BaseModel, id_generator


class UserModel(BaseModel):
    """
    UserModel is a SQLAlchemy model representing a user in the database.

    Attributes:
        id (str): The unique identifier for the user.
        name (str): The name of the user.
        gender (str): The gender of user, represented as a single character
        birth_date (datetime): The birth date of the user in a string format.
        state (str): The state where the user resides, represented as a two-character code.
        city (str): The city where the user resides.
        cep (str): The postal code (CEP) of the user's address.
        complement (str): Additional address information, if any.
        email (str): The email address of the user, must be unique.
        password (str): The hashed password of the user.
        created_at (datetime): Timestamp when the user record was created.
        updated_at (datetime): Timestamp when the user record was last updated.
    """
    
    __tablename__ = 'users'

    id: Mapped[str] = mapped_column(String,primary_key=True, default=id_generator)
    name: Mapped[str] = mapped_column(String(255), nullable=True)
    gender: Mapped[str] = mapped_column(String(1), nullable=True)
    birth_date: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)
    state: Mapped[str] = mapped_column(String(2), nullable=True)
    city: Mapped[str] = mapped_column(String(50), nullable=True)
    cep: Mapped[str] = mapped_column(String(10), nullable=True)
    complement: Mapped[str] = mapped_column(Text, nullable=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )