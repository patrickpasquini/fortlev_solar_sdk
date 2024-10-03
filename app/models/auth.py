from dataclasses import dataclass


@dataclass
class Auth:
    access_token: str
    scope: str
    token_type: str
