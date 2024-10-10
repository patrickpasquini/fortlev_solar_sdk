from dataclasses import dataclass
import datetime


@dataclass
class Auth:
    """
    Represents authentication details required for API access.

    Attributes:
        access_token (str): The token used to authenticate API requests.
        scope (str): The specific scope of access granted by the token.
        token_type (str): The type of the token, defaulting to 'Bearer'.
        _expiry_time (datetime): The datetime at which the token expires.
    """

    access_token: str
    scope: str
    token_type: str = "Bearer"
    _expiry_time: datetime.datetime = datetime.datetime.now() + datetime.timedelta(
        hours=24
    )

    def is_expired(self) -> bool:
        """
        Checks if the authentication token has expired.

        Returns:
            bool: Returns True if the token has expired, otherwise False.
        """
        return datetime.datetime.now() >= self._expiry_time
