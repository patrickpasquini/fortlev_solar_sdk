from dataclasses import dataclass


@dataclass
class City:
    """
    Represents a city with geographic and administrative details.

    Attributes:
        id (str): The unique identifier for the city.
        name (str): The name of the city.
        ibge_code (str): The IBGE code associated with the city.
        isopleth (int): The isopleth value indicating a specific attribute of the city.
        latitude (float): The latitude coordinate of the city.
        longitude (float): The longitude coordinate of the city.
        distribution_center (str) : The distribuiton center that serves the city
    """

    id: str
    name: str
    ibge_code: str
    isopleth: int
    latitude: float
    longitude: float
    distribution_center: str

    @classmethod
    def from_dict(cls, data: dict) -> "City":
        """
        Creates a City instance from a dictionary.

        Args:
            data (dict): A dictionary containing city details.

        Returns:
            City: A new City instance with attributes populated from the dictionary.
        """
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            ibge_code=data.get("ibge_code"),
            isopleth=data.get("isopleth"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            distribution_center=data.get("distribution_center"),
        )
