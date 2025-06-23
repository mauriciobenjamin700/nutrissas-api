from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

class BaseModel(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    #__sa_dataclass_metadata_key__ = "sa"
    # Adicione campos/métodos comuns aqui, se necessário

    def to_dict(self, exclude: list[str] = [], include: dict = {}) -> dict:
        """
            Converts the model instance to a dictionary.

            Args:
                exclude (list[str]): List of field names to exclude from the dictionary.
                include (dict): Dictionary of additional fields to include in the output.

            Returns:
                dict: A dictionary representation of the model instance, excluding specified fields and including additional fields.
        """
        data =  {column.name: getattr(self, column.name) for column in self.__table__.columns}

        for field in exclude:
            data.pop(field, None)

        if include:
            data.update(include)

        return data

class DatabaseHandler:
    """
    DatabaseHandler is a class that manages the connection to the database using SQLAlchemy's async capabilities.

    Attributes:
        engine (AsyncEngine): The SQLAlchemy async engine for database connections.
        async_session (async_sessionmaker): A session factory for creating async sessions.

    Methods:
        get_session: An async generator that provides a session for database operations.
        close: Closes the database engine connection.
        create_tables: Creates all tables defined in the SQLAlchemy models.
        drop_tables: Drops all tables defined in the SQLAlchemy models.
    """
    def __init__(self, database_url: str):
        self.engine = create_async_engine(database_url, echo=True)
        self.async_session = async_sessionmaker(
            self.engine,
            expire_on_commit=False,
            class_=AsyncSession
        )

    async def get_session(self) -> AsyncSession: # type: ignore
        """
        Provides an async session for database operations.

        Args:
            None

        Yields:
            AsyncSession: An async session for executing database operations.
        """
        async with self.async_session() as session:
            yield session

    async def close(self) -> None:
        """
        Properly closes the database engine connection.

        Args:
            None

        Returns:
            None
        """
        await self.engine.dispose()

    async def create_tables(self) -> None:
        """
        Creates all tables defined in the SQLAlchemy models.

        Args:
            None

        Returns:
            None
        """
        async with self.engine.begin() as conn:
            from src.db.models import (
                FoodModel,
                MedicalHistoryModel,
                TrainModel,
                MealModel,
                DietModel,
                ExerciseModel,
                UserModel
            )
            await conn.run_sync(BaseModel.metadata.create_all)

    async def drop_tables(self) -> None:
        """
        Drops all tables defined in the SQLAlchemy models.

        Args:
            None

        Returns:
            None
        """
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)