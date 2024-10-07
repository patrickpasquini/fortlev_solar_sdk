from .base_classes import Identity
from dataclasses import dataclass


@dataclass
class Surface(Identity):
    """
    Represents a surface used in a PV kit installation, inheriting from Identity.

    Inherits from:
        Identity: Provides attributes such as id, name, and family.

    Methods:
        from_dict (dict): Creates an instance of Surface from a dictionary.
    """

    @classmethod
    def from_dict(cls, data: dict) -> "Surface":
        """
        Creates an instance of Surface from a dictionary.

        Args:
            data (dict): A dictionary containing surface information.

        Returns:
            Surface: An instance of the Surface class.
        """
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            family=data.get("family"),
        )
