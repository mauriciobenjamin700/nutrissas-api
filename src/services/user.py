from sqlalchemy.ext.asyncio import AsyncSession

from src.db.repositories import UserRepository


class UserService:
    def __init__(self, db: AsyncSession) -> None:
        self.repository = UserRepository(db)
        # TODO: IMPLEMENT USER SERVICE METHODS
    