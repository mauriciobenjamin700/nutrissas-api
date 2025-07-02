from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.dependencies import get_current_user, get_db_session
from src.schemas import TokenResponse, UserCreate, UserLogin, UserResponse
from src.services import UserService

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/")
async def add_user(
    request: UserCreate,
    db_session: AsyncSession = Depends(get_db_session),
) -> UserResponse:
    """
    Endpoint to add a new user.

    Args:
        request (UserCreate): The user creation request data.
        user_service (UserService): The user service dependency.

    Returns:
        UserResponse: The created user response.
    """

    user_service = UserService(db_session)
    return await user_service.add_user(request)


@router.get("/")
async def get_user_by_token(
    user: UserResponse = Depends(get_current_user),
) -> UserResponse:
    """
    Endpoint to get a user by ID.

    Args:
        user_id (str): The ID of the user to retrieve.
        db_session (AsyncSession): The database session dependency.

    Returns:
        UserResponse: The retrieved user response.
    """

    return user


@router.post("/login")
async def login_user(
    request: UserLogin,
    db_session: AsyncSession = Depends(get_db_session),
) -> TokenResponse:
    """
    Endpoint to login a user.

    Args:
        request (UserLogin): The user login request data.
        db_session (AsyncSession): The database session dependency.

    Returns:
        UserResponse: The logged-in user response.
    """

    user_service = UserService(db_session)
    return await user_service.login(request)


@router.post("/auth")
async def authenticate_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db_session: AsyncSession = Depends(get_db_session),
) -> TokenResponse:
    """
    Endpoint to authenticate a user by ID.

    Args:
        user_id (str): The ID of the user to authenticate.
        db_session (AsyncSession): The database session dependency.

    Returns:
        UserResponse: The authenticated user response.
    """

    service = UserService(db_session)

    login_data = UserLogin(
        email=form_data.username, password=form_data.password
    )
    token_response = await service.login(login_data)

    return token_response