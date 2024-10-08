from fortlev_solar_sdk import FortlevSolarClient
from fortlev_solar_sdk.surface import Surface


def test_get_surfaces(client: FortlevSolarClient):
    """
    Test retrieving surface data using the FortlevSolarClient.

    This test verifies the functionality of the `surfaces` method in the FortlevSolarClient.
    It checks that when the method is called, it returns exactly 10 `Surface` objects.

    Args:
        client (FortlevSolarClient): An instance of the FortlevSolarClient.
    """
    surfaces = client.surfaces()
    assert len(surfaces) == 10
    assert type(surfaces[0]) == Surface
