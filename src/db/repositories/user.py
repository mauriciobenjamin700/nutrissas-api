from fastapi import HTTPException
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import messages
from src.db.models import UserModel
from src.schemas import UserCreate, UserResponse

class UserRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def add_user(self, model: UserModel) -> UserModel:
        """
        Adds a new user to the database.

        Args:
            model (UserModel): The user model to be added.

        Returns:
            UserModel: The added user model.
        """

        stmt = select(UserModel).where(UserModel.email == model.email)
        result = await self.db.execute(stmt)
        existing_user = result.unique().scalars().first()

        if existing_user:
            raise HTTPException(
                status_code=409,
                detail=messages.USER_EMAIL_ALREADY_EXISTS
            )

        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)
        return model
    
    async def get_user(
        self,
        user_id: str | None = None,
        email: str | None = None,
        all_results: bool = False
    ) -> list[UserModel] | UserModel | None:
        """
        Retrieves a user from the database by ID or email.

        Args:
            user_id (str | None): The ID of the user to retrieve.
            email (str | None): The email of the user to retrieve.
            all_results (bool): If True, returns all matching users; otherwise, returns a single user.

        Returns:
            list[UserModel] | UserModel | None: The retrieved user(s) or None if not found.
        """
        query = select(UserModel)
        
        if user_id:
            query = query.where(UserModel.id == user_id)
        elif email:
            query = query.where(UserModel.email == email)
        
        result = await self.db.execute(query)
        
        if all_results:
            return result.unique().scalars().all()
        
        return result.unique().scalars().first()
    

    async def update(self, model: UserModel) -> UserModel:
        """
        Updates an existing user in the database.

        Args:
            model (UserModel): The user model with updated data.

        Returns:
            UserModel: The updated user model.
        """
        await self.db.commit()
        await self.db.refresh(model)
        return model
    
    async def delete(self, user_id: str) -> bool:
        """
        Deletes a user from the database by ID.

        Args:
            user_id (str): The ID of the user to delete.

        Returns:
            None
        """
        query = delete(UserModel).where(UserModel.id == user_id)
        result = await self.db.execute(query)
        await self.db.commit()
        return result.rowcount > 0
    

    def map_request_to_model(self, request: UserCreate) -> UserModel:
        """
        Maps a UserCreate request to a UserModel.

        Args:
            request (UserCreate): The user creation request.

        Returns:
            UserModel: The mapped user model.
        """
        return UserModel(
            **request.to_dict()
        )
    
    def map_model_to_response(self, model: UserModel) -> UserResponse:
        return UserResponse.model_validate(model, from_attributes=True)