from dataclasses import dataclass


@dataclass
class RegisterResponse:
    message: str
    is_valid: bool
