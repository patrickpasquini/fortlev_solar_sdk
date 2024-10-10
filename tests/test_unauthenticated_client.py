from fortlev_solar_sdk import FortlevSolarClient
from fortlev_solar_sdk.errors import RequestError
import pytest


def test_unauthenticated_client():
    """
    Test if the FortlevSolarClient raises a RequestError when attempting to fetch orders
    without authentication.

    This test creates an instance of the FortlevSolarClient without authenticating the user.
    It then calls the orders() method, which should raise a RequestError with a 401 status code
    and a specific message indicating that the user is not authenticated.

    Raises:
        RequestError: When the client tries to access the orders endpoint without prior authentication.

    Asserts:
        The raised error matches the expected error message and status code.
    """
    unauthenticated_client = FortlevSolarClient()
    with pytest.raises(
        RequestError,
        match="Request Error 401. User is not authenticated. Please call authenticate().",
    ):
        unauthenticated_client.orders()
