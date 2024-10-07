from dataclasses import dataclass


@dataclass
class Summary:
    """
    Represents a summary of an order with pricing and power details.

    Attributes:
        final_price (float): The final price after any discounts.
        full_price (float): The original full price before any discounts.
        discount (float): The discount applied to the full price.
        power (float): The power output associated with the order.
    """

    final_price: float
    full_price: float
    discount: float
    power: float


@dataclass
class Identity:
    """
    Represents an entity with a unique identity.

    Attributes:
        id (str): The unique identifier for the entity.
        name (str): The name of the entity.
        family (str): The family or category to which the entity belongs.
    """

    id: str
    name: str
    family: str


@dataclass
class File:
    """
    Represents a file with storage details.

    Attributes:
        key (str): The unique key used to identify the file.
        path (str): The path where the file is stored.
    """

    key: str
    path: str

    @classmethod
    def from_dict(cls, data: dict) -> "File":
        """
        Creates a File instance from a dictionary.

        Args:
            data (dict): A dictionary containing file details.

        Returns:
            File: A new File instance with attributes populated from the dictionary.
        """
        return cls(key=data.get("key"), path=data.get("path"))
