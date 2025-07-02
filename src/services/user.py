from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import SecurityHandler
from src.core import messages
from src.db.repositories import UserRepository
from src.schemas import (
    TokenData, 
    TokenResponse, 
    MessageResponse, 
    UserCreate, 
    UserLogin, 
    UserResponse
)

class UserService:
    """
    UserService is responsible for handling user-related operations,

    Methods:
        add_user: Adds a new user to the database.
        get_user: Retrieves a user by ID or email.
    """
    def __init__(self, db: AsyncSession) -> None:
        self.repository = UserRepository(db)
    
    async def add_user(self, request: UserCreate) -> UserResponse:
        """
        Adds a new user to the database.

        Args:
            request (UserCreate): The user creation request data.

        Returns:
            UserResponse: The created user response.
        """
        
        request.password = SecurityHandler.hash_password(request.password)

        model = self.repository.map_request_to_model(request)

        model = await self.repository.add_user(model)

        response = self.repository.map_model_to_response(model)

        return response
    

    async def get_user_by_id(self, user_id: str) -> UserResponse:
        """
        Retrieves a user by ID.

        Args:
            user_id (str): The ID of the user to retrieve.

        Returns:
            UserResponse | None: The retrieved user response or None if not found.
        """
        model = await self.repository.get_user(user_id=user_id)
        
        if model is None:
            raise HTTPException(
                status_code=404,
                detail=messages.USER_NOT_FOUND
            )
        
        return self.repository.map_model_to_response(model)
    

    async def get_user_by_email(self, email: str) -> UserResponse:
        """
        Retrieves a user by email.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            UserResponse | None: The retrieved user response or None if not found.
        """
        model = await self.repository.get_user(email=email)
        
        if model is None:
            raise HTTPException(
                status_code=404,
                detail=messages.USER_NOT_FOUND
            )
        
        return self.repository.map_model_to_response(model)
    

    async def get_all_users(self) -> list[UserResponse]:
        """
        Retrieves all users.

        Returns:
            list[UserResponse]: A list of all user responses.
        """
        models = await self.repository.get_user(all_results=True)
        
        return [self.repository.map_model_to_response(model) for model in models]
    

    async def delete_user(self, user_id: str) -> MessageResponse:
        """
        Deletes a user by ID.

        Args:
            user_id (str): The ID of the user to delete.

        Raises:
            HTTPException: If the user is not found.
        """
        result = await self.repository.delete(user_id=user_id)
        
        if not result:
            raise HTTPException(
                status_code=404,
                detail=messages.USER_NOT_FOUND
            )
        
        return MessageResponse(detail=messages.SUCCESS_DELETE_USER)
    

    async def login(self, request: UserLogin) -> TokenResponse:
        """
        Logs in a user by validating credentials.

        Args:
            request (UserLogin): The user login request data.

        Returns:
            UserResponse: The logged-in user response.

        Raises:
            HTTPException: If the user is not found or password is incorrect.
        """
        model = await self.repository.get_user(email=request.email)
        
        if model is None:
            raise HTTPException(
                status_code=404,
                detail=messages.USER_NOT_FOUND
            )
        
        if not SecurityHandler.verify_password(request.password, model.password):
            raise HTTPException(
                status_code=401,
                detail=messages.WRONG_USER_PASSWORD
            )
        
        user = self.repository.map_model_to_response(model)

        token_data = TokenData(sub=user.id,)

        token = SecurityHandler.create_jwt_token(token_data.to_dict())

        return TokenResponse(
            access_token=token,
            user=user
        )