from fortlev_solar_sdk import FortlevSolarClient
from fortlev_solar_sdk.financing import Financing


def test_create_simplified_financing(client: FortlevSolarClient):
    """Tests the financing method of the FortlevSolarClient.

    This test verifies that the financing method successfully retrieves
    financing options based on the provided investment value.

    Args:
        client (FortlevSolarClient): An instance of the FortlevSolarClient.
    """
    financing_result = client.financing(value=10000)
    assert len(financing_result) > 1
    assert isinstance(financing_result[0], Financing)
