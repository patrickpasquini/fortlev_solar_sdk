from fortlev_solar_sdk import FortlevSolarClient
from fortlev_solar_sdk.order import Order


def test_create_orders(client: FortlevSolarClient):
    """
    Test the creation of orders using the FortlevSolarClient.

    This test verifies that the `orders` method of the FortlevSolarClient returns
    a list of `Order` objects with at least one item. The test ensures that:
    - The list of orders is not empty.
    - The returned objects are of type `Order`.

    Args:
        client (FortlevSolarClient): The authenticated client fixture used to interact
        with the Fortlev Solar API.
    """
    orders = client.orders()
    assert len(orders) > 1
    assert type(orders[0]) == Order
