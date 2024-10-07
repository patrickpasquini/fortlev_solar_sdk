class BaseError(Exception):
    """
    A base class for custom exceptions in the SDK.

    Attributes:
        status_code (int): The HTTP status code associated with the error.
        error_message (str): A descriptive message explaining the error.
    """

    def __init__(self, status_code: int, error_message: str) -> None:
        self.status_code = status_code
        self.error_message = error_message


class RequestError(BaseError):
    """
    An exception for errors encountered during HTTP requests.

    Inherits from:
        BaseError: Provides the status code and error message attributes.

    Attributes:
        status_code (int): The HTTP status code associated with the request error.
        error_message (str): A descriptive message explaining the request error.
    """

    def __init__(self):
        message = f"{self.error_message}. Request error: {self.status_code}"
        super().__init__(message)
