from src.db import db


async def get_db_session():
    """
    Dependency to get the database session.

    Args:
        None

    Returns:
        AsyncSession: An async session for executing database operations.
    """
    async for session in db.get_session():
        yield session