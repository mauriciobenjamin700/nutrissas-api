import bcrypt
from jose import jwt

from src.core.settings import settings


class SecurityHandler:

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hashes a password using bcrypt.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Verifies a plain password against a hashed password.

        Args:
            plain_password (str): The plain password to verify.
            hashed_password (str): The hashed password to compare against.

        Returns:
            bool: True if the passwords match, False otherwise.
        """
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    

    @staticmethod
    def create_jwt_token(
        data: dict, 
        expires_delta: int = 3600 * 24 * 30  # Default to 30 days
    ) -> str:
        """
        Creates a JWT token.

        Args:
            data (dict): The payload data to include in the token.
            expires_delta (int): The expiration time in seconds.

        Returns:
            str: The generated JWT token.
        """
        to_encode = data.copy()
        to_encode.update({"exp": jwt.datetime.utcnow() + jwt.timedelta(seconds=expires_delta)})
        return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    

    @staticmethod
    def decode_jwt_token(token: str) -> dict:
        """
        Decodes a JWT token.

        Args:
            token (str): The JWT token to decode.

        Returns:
            dict: The decoded payload data.
        """
        return jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
    