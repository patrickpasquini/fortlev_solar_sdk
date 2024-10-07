from .base_classes import Identity, File
from dataclasses import dataclass


@dataclass
class Component(Identity):
    """
    Represents a component with identifying details and associated files.

    Inherits from:
        Identity: Includes basic identity attributes such as id, name, and family.

    Attributes:
        code (str): The unique code assigned to the component.
        attachments (list[File]): A list of File instances associated with the component.
    """

    code: str
    attachments: list[File]

    @classmethod
    def from_dict(cls, data: dict) -> "Component":
        """
        Creates a Component instance from a dictionary.

        Args:
            data (dict): A dictionary containing component details.

        Returns:
            Component: A new Component instance with attributes populated from the dictionary.
        """
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            code=data.get("code"),
            family=data.get("family"),
            attachments=[
                File.from_dict(attachment) for attachment in data.get("attachments", [])
            ],
        )
