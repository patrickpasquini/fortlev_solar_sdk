from fortlev_solar_sdk import FortlevSolarClient
from fortlev_solar_sdk.component import Component


def test_get_components(client: FortlevSolarClient):
    """
    Test retrieving component data using the FortlevSolarClient.

    This test verifies the functionality of the `components` method in the FortlevSolarClient.
    It checks two scenarios:
    - When no filters are applied, it ensures that exactly 10 `Component` objects are returned.
    - When pagination parameters are applied with `query_params`, it checks that the correct
      number of components is returned based on the specified page size.

    Args:
        client (FortlevSolarClient): The authenticated client fixture used to interact with
        the Fortlev Solar API.
    """
    components = client.components()
    assert len(components) == 10
    assert type(components[0]) == Component

    query = {"docs_per_page": 20, "current_page": 1}
    components = client.components(query_params=query)
    assert len(components) == 20
