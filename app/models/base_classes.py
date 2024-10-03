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
