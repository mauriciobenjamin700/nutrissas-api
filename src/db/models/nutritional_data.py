from datetime import datetime
from sqlalchemy import String, Text, TIMESTAMP, ForeignKey, DECIMAL, func
from sqlalchemy.orm import Mapped, mapped_column


from src.core import BaseModel, get_current_time, id_generator


class NutritionalDataModel(BaseModel):
    """
    NutritionalDataModel is a SQLAlchemy model representing nutritional data for a user in the database.

    Attributes:
        id (str): The unique identifier for the nutritional data entry.
        user_id (str): The ID of the user to whom this nutritional data belongs.
        weight (float): The weight of the user in kilograms.
        height (float): The height of the user in centimeters.
        cmi (float): The calculated CMI (Body Mass Index).
        evaluation_date (str): The date of the nutritional evaluation.
        skinfolds (str): Skinfold measurements as a JSON string.
        circumferences (str): Circumference measurements as a JSON string.
        allergies (str): Allergies information as a text string.
        goal (str): The user's nutritional goal.
        monthly_budget (float): The user's monthly budget for nutrition.
        created_at (str): Timestamp when the record was created.
        updated_at (str): Timestamp when the record was last updated.
    """
    
    __tablename__ = 'nutritional_data'

    id: Mapped[str] = mapped_column(String,primary_key=True, default=id_generator)
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'), nullable=False)
    weight: Mapped[float] = mapped_column(DECIMAL, nullable=False)
    height: Mapped[float] = mapped_column(DECIMAL, nullable=False)
    cmi: Mapped[float] = mapped_column(DECIMAL, nullable=False)
    evaluation_date: Mapped[str] = mapped_column(TIMESTAMP, nullable=False)
    skinfolds: Mapped[str] = mapped_column(String, nullable=True)
    circumferences: Mapped[str] = mapped_column(String, nullable=True)
    allergies: Mapped[str] = mapped_column(Text, nullable=True)
    goal: Mapped[str] = mapped_column(String, nullable=True)
    monthly_budget: Mapped[float] = mapped_column(DECIMAL, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )