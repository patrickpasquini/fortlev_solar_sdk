class BaseError(Exception):
    """
    A base class for custom exceptions in the SDK.

    Attributes:
        status_code (int): The HTTP status code associated with the error.
        error_message (str): A descriptive message explaining the error.
    """

    def __init__(self, status_code: int, error_message: str) -> None:
        self.error_message = error_message
        self.status_code = status_code

    def __str__(self):
        return f"Error {self.status_code}. {self.error_message}"


class RequestError(BaseError):
    """
    An exception for errors encountered during HTTP requests.

    Inherits from:
        BaseError: Provides the status code and error message attributes.

    Attributes:
        status_code (int): The HTTP status code associated with the request error.
        error_message (str): A descriptive message explaining the request error.
    """

    def __init__(self, error_message: str, status_code: int) -> None:
        super().__init__(status_code=status_code, error_message=error_message)

    def __str__(self):
        return f"Request Error {self.status_code}. {self.error_message}"
