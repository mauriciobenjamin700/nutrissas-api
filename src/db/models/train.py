from datetime import datetime
from sqlalchemy import Integer, String, Text, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column


from src.core import BaseModel, get_current_time, id_generator


class TrainModel(BaseModel):
    """
    TrainModel is a SQLAlchemy model representing a training session for an exercise in the database.
    
    Attributes:
        id (str): The unique identifier for the train entry.
        exercise_id (str): The ID of the exercise associated with this train entry.
        user_id (str): The ID of the user who performed the train.
        date (datetime): The date and time when the train was performed.
        duration (int): The duration of the train in minutes.
        goal (str): The goal of the train, if any.
        created_at (datetime): Timestamp when the record was created.
        updated_at (datetime): Timestamp when the record was last updated.
    """
     
    __tablename__ = 'trains'

    id: Mapped[str] = mapped_column(String,primary_key=True, default=id_generator)
    exercise_id: Mapped[str] = mapped_column(ForeignKey('exercises.id'), nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'), nullable=False)
    date: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
    duration: Mapped[int] = mapped_column(Integer, nullable=False)
    goal: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

