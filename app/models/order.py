from .base_classes import Summary
from .pv_kit import PvKit
from dataclasses import dataclass


@dataclass
class Order(Summary):
    pv_kits: list[PvKit]
    delivery_at: str
