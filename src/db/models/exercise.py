from datetime import datetime
from sqlalchemy import DECIMAL, Integer, String, Text, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column


from src.core import BaseModel, get_current_time, id_generator


class ExerciseModel(BaseModel):
    """
    ExerciseModel is a SQLAlchemy model representing an exercise record in the database.
    
    Attributes:
        id (str): The unique identifier for the exercise.
        name (str): The name of the exercise.
        description (str): A description of the exercise.
        tip (str): Tips for performing the exercise.
        series (int): The number of series to perform.
        repetitions (str): The number of repetitions for each series.
        muscle_group (str): The muscle group targeted by the exercise.
        is_completed (bool): Indicates if the exercise has been completed.
        weight (float): The weight used during the exercise, if applicable.
        created_at (datetime): Timestamp when the record was created.
        updated_at (datetime): Timestamp when the record was last updated.
    """
     
    __tablename__ = 'exercises'

    id: Mapped[str] = mapped_column(String,primary_key=True, default=id_generator)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    tip: Mapped[str] = mapped_column(Text, nullable=True)
    series: Mapped[int] = mapped_column(Integer, nullable=False)
    repetitions: Mapped[str] = mapped_column(String, nullable=False)
    muscle_group: Mapped[str] = mapped_column(String, nullable=False)
    is_completed: Mapped[bool] = mapped_column(nullable=False, default=False)
    weight: Mapped[float] = mapped_column(DECIMAL, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )