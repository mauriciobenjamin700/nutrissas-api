from datetime import datetime
from sqlalchemy import String, Text, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column


from src.core import BaseModel, get_current_time, id_generator


class MedicalHistoryModel(BaseModel):
    """
    MedicalHistoryModel is a SQLAlchemy model representing a user's medical history in the database.
    
    Attributes:
        id (str): The unique identifier for the medical history entry.
        user_id (str): The ID of the user to whom this medical history belongs.
        have_illness (bool): Indicates if the user has any illness.
        illness (str): The name of the illness, if applicable.
        illness_description (str): A description of the illness, if applicable.
        medical_record_file_path (str): Path to a file containing medical records, if applicable.
        created_at (str): Timestamp when the record was created.
        updated_at (str): Timestamp when the record was last updated.
    """
    
    __tablename__ = 'medical_history'

    id: Mapped[str] = mapped_column(String,primary_key=True, default=id_generator)
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'), nullable=False)
    have_illness: Mapped[bool] = mapped_column(nullable=False, default=False)
    illness: Mapped[str] = mapped_column(String, nullable=True)
    illness_description: Mapped[str] = mapped_column(Text, nullable=True)
    medical_record_file_path: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )