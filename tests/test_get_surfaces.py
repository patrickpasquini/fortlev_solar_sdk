from app.models import FortlevSolarClient


def test_get_surfaces(client: FortlevSolarClient):
    response = client.surfaces()
    print(response)
