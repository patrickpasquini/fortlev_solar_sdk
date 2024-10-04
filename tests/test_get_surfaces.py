from fortlev_solar_sdk import FortlevSolarClient
from fortlev_solar_sdk.surface import Surface


def test_get_surfaces(client: FortlevSolarClient):
    surfaces = client.surfaces()
    assert len(surfaces) == 10
    assert type(surfaces[0]) == Surface
