from fortlev_solar_sdk import FortlevSolarClient
from fortlev_solar_sdk.order import Order


def test_create_orders(client: FortlevSolarClient):
    orders = client.orders()
    assert len(orders) > 1
    assert type(orders[0]) == Order
