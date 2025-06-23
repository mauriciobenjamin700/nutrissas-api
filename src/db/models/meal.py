from datetime import datetime
from sqlalchemy import ForeignKey, String, TIMESTAMP, Text, func
from sqlalchemy.orm import Mapped, mapped_column


from src.core import BaseModel, get_current_time, id_generator


class MealModel(BaseModel):
    """
    MealModel is a SQLAlchemy model representing a meal record for a user in the database.
    
    Attributes:
        id (str): The unique identifier for the meal.
        food_id (str): The ID of the food item associated with this meal.
        diet_id (str): The ID of the diet associated with this meal.
        type (str): The type of meal (e.g., 'breakfast', 'lunch', 'dinner').
        is_completed (bool): Indicates if the meal has been completed.
        description (str): A description of the meal.
        created_at (datetime): Timestamp when the record was created.
        updated_at (datetime): Timestamp when the record was last updated.
    """
     
    __tablename__ = 'meals'

    id: Mapped[str] = mapped_column(String,primary_key=True, default=id_generator)
    food_id: Mapped[str] = mapped_column(ForeignKey('foods.id'), nullable=False)
    diet_id: Mapped[str] = mapped_column(ForeignKey('diets.id'), nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    is_completed: Mapped[bool] = mapped_column(nullable=False, default=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )