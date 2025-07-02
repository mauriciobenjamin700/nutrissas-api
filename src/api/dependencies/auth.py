from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.dependencies.database import get_db_session
from src.core import SecurityHandler
from src.schemas import TokenData, UserResponse
from src.services import UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/auth")

async def get_current_user(
        token: str = Depends(oauth2_scheme),
        db_session: AsyncSession = Depends(get_db_session),
    ) -> UserResponse:
    """
    Dependency to get the current user based on the provided OAuth2 token.

    Args:
        token (str): The OAuth2 token provided by the user.

    Returns:
        str: The user identifier extracted from the token.
    """
    payload = SecurityHandler.decode_jwt_token(token)
    data = TokenData(**payload)

    service = UserService(db_session)

    user = await service.get_user_by_id(user_id=data.sub)

    return user
