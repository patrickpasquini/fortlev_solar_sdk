from fortlev_solar_sdk import FortlevSolarClient
from fortlev_solar_sdk.city import City


def test_get_components(client: FortlevSolarClient):
    cities = client.cities()
    assert len(cities) == 10
    assert type(cities[0]) == City
    query = {"slug_name_eq": "vitoria"}
    cities = client.cities(query_params=query)
    assert len(cities) == 1
