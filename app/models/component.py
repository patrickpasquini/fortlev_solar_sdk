from .base_classes import Identity
from dataclasses import dataclass


@dataclass
class Component(Identity):
    code: str

    @classmethod
    def from_dict(cls, component_data: dict):
        return cls(
            id=component_data["id"],
            name=component_data["name"],
            family=component_data["code"],
            family=component_data["family"],
        )
