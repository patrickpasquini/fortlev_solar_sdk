from dataclasses import dataclass


@dataclass
class Summary:
    final_price: float
    full_price: float
    discount: float
    power: float


@dataclass
class Identity:
    id: str
    name: str
    family: str


@dataclass
class File:
    key: str
    path: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(key=data.get("key"), path=data.get("path"))
