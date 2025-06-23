from datetime import datetime
from sqlalchemy import DECIMAL, String, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column


from src.core import BaseModel, get_current_time, id_generator


class FoodModel(BaseModel):
    """
    FoodModel is a SQLAlchemy model representing a food item in the database.
    
    Attributes:
        id (str): The unique identifier for the food item.
        name (str): The name of the food item.
        quantity (float): The quantity of the food item.
        calories (float): The number of calories in the food item.
        proteins (float): The amount of protein in the food item.
        fats (float): The amount of fat in the food item.
        carbohydrates (float): The amount of carbohydrates in the food item.
        consumption_date (datetime): The date when the food was consumed.
        type (str): The type of food (e.g., 'breakfast', 'lunch', 'dinner').
        created_at (datetime): Timestamp when the record was created.
        updated_at (datetime): Timestamp when the record was last updated.
    """
     
    __tablename__ = 'foods'

    id: Mapped[str] = mapped_column(String,primary_key=True, default=id_generator)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    quantity: Mapped[float] = mapped_column(DECIMAL, nullable=False)
    calories: Mapped[float] = mapped_column(DECIMAL, nullable=False)
    proteins: Mapped[float] = mapped_column(DECIMAL, nullable=False)
    fats: Mapped[float] = mapped_column(DECIMAL, nullable=False)
    carbohydrates: Mapped[float] = mapped_column(DECIMAL, nullable=False)
    consumption_date: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )