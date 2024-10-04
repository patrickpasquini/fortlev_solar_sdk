from .base_classes import Identity
from dataclasses import dataclass


@dataclass
class Surface(Identity):

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            family=data.get("family"),
        )
