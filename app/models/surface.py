from .base_classes import Identity
from dataclasses import dataclass


@dataclass
class Surface(Identity):

    @classmethod
    def from_dict(cls, surface_data: dict):
        return cls(
            id=surface_data["id"],
            name=surface_data["name"],
            family=surface_data["family"],
        )
