from fortlev_solar_sdk import FortlevSolarClient
from dotenv import load_dotenv
import pytest
import os

load_dotenv()

USERNAME = os.getenv("FORTLEV_SOLAR_USERNAME")
PWD = os.getenv("FORTLEV_SOLAR_PWD")


@pytest.fixture(scope="session")
def client():
    """
    Fixture to initialize and authenticate a FortlevSolarClient instance.

    This fixture provides an authenticated FortlevSolarClient instance for use
    in tests that require API interaction. The client is initialized once per session
    to avoid redundant authentication requests.

    Returns:
        FortlevSolarClient: An authenticated instance of the client.
    """
    client = FortlevSolarClient()
    client.authenticate(username=USERNAME, pwd=PWD)
    return client
