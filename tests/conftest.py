from fortlev_solar_sdk import FortlevSolarClient
from dotenv import load_dotenv
import pytest
import os

load_dotenv()

USERNAME = os.getenv("FORTLEV_SOLAR_USERNAME")
PWD = os.getenv("FORTLEV_SOLAR_PWD")


@pytest.fixture(scope="session")
def client():
    client = FortlevSolarClient()
    client.authenticate(username=USERNAME, pwd=PWD)
    return client
