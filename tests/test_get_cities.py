from fortlev_solar_sdk import FortlevSolarClient
from fortlev_solar_sdk.city import City


def test_get_components(client: FortlevSolarClient):
    """
    Test retrieving city data using the FortlevSolarClient.

    This test verifies the functionality of the `cities` method in the FortlevSolarClient.
    It checks two scenarios:
    - When no filters are applied, it ensures that exactly 10 `City` objects are returned.
    - When a filter is applied with `query_params`, it checks that the correct number of cities
      matching the filter is returned.

    Args:
        client (FortlevSolarClient): The authenticated client fixture used to interact with
        the Fortlev Solar API.
    """
    cities = client.cities()
    assert len(cities) == 10
    assert type(cities[0]) == City

    query = {"slug_name_eq": "vitoria"}
    cities = client.cities(query_params=query)
    assert len(cities) == 1
