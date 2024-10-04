from fortlev_solar_sdk import FortlevSolarClient
from fortlev_solar_sdk.component import Component


def test_get_components(client: FortlevSolarClient):
    components = client.components()
    assert len(components) == 10
    assert type(components[0]) == Component
    query = {"docs_per_page": 20, "current_page": 1}
    components = client.components(query_params=query)
    assert len(components) == 20
