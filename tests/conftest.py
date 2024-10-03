from app.models import FortlevSolarClient
import pytest


@pytest.fixture(scope="session")
def client():
    client = FortlevSolarClient()
    client.authenticate(username="contato@fortlevsolar.com.br", pwd="F@rtlev40!")
    return client
