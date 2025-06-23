from datetime import datetime
from sqlalchemy import DECIMAL, ForeignKey, String, TIMESTAMP, Text, func
from sqlalchemy.orm import Mapped, mapped_column


from src.core import BaseModel, get_current_time, id_generator


class DietModel(BaseModel):
    """
    DietModel is a SQLAlchemy model representing a diet record for a user in the database.
    
    Attributes:
        id (str): The unique identifier for the diet.
        user_id (str): The ID of the user to whom this diet belongs.
        date (datetime): The date and time when the diet was recorded.
        total_calories (float): The total calories consumed in the diet.
        total_proteins (float): The total proteins consumed in the diet.
        total_fats (float): The total fats consumed in the diet.
        total_carbohydrates (float): The total carbohydrates consumed in the diet.
        total_water (float): The total water consumed in the diet.
        duration (int): The duration of the diet in minutes.
        created_at (datetime): Timestamp when the record was created.
        updated_at (datetime): Timestamp when the record was last updated.
    """
     
    __tablename__ = 'diets'

    id: Mapped[str] = mapped_column(String,primary_key=True, default=id_generator)
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'), nullable=False)
    date: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
    total_calories: Mapped[float] = mapped_column(DECIMAL,nullable=False)
    total_proteins: Mapped[float] = mapped_column(DECIMAL, nullable=False)
    total_fats: Mapped[float] = mapped_column(DECIMAL, nullable=False)
    total_carbohydrates: Mapped[float] = mapped_column(DECIMAL, nullable=False)
    total_water: Mapped[float] = mapped_column(DECIMAL, nullable=False)
    duration: Mapped[int] = mapped_column(nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
