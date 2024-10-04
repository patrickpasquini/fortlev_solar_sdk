class BaseError(Exception):
    def __init__(self, status_code: int, error_message: str) -> None:
        self.status_code = status_code
        self.error_message = error_message


class RequestError(BaseError):

    def __init__(self):
        message = f"{self.error_message}. Request error: {self.status_code}"
        super().__init__(message)
