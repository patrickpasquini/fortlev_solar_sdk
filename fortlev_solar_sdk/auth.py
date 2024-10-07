from dataclasses import dataclass


@dataclass
class Auth:
    """
    Represents authentication details required for API access.

    Attributes:
        access_token (str): The token used to authenticate API requests.
        scope (str): The specific scope of access granted by the token.
        token_type (str): The type of the token, defaulting to 'Bearer'.
    """

    access_token: str
    scope: str
    token_type: str = "Bearer"
