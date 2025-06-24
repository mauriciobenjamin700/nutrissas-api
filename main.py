import asyncio
import uvicorn

from src.api import app
from src.core import DatabaseHandler

def create_tables():
    """
    Creates all tables defined in the SQLAlchemy models.
    
    This function is a wrapper around the DatabaseHandler's create_tables method.
    It runs the asynchronous create_tables method in an event loop.
    
    Returns:
        None
    """
    async def run_create_tables():
        db = DatabaseHandler("sqlite+aiosqlite:///.database.db")
        await db.create_tables()

    asyncio.run(run_create_tables())


create_tables()

uvicorn.run(
    app,
    host="0.0.0.0",
    port=8004,
    log_level="info",
)