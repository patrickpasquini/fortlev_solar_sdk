from dataclasses import dataclass
from .base_classes import Summary, File
from .surface import Surface
from .component import Component


@dataclass
class Layout:
    line_quantity: int
    modules_per_line: int
    line_length: float

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            line_quantity=data.get("line_quantity"),
            modules_per_line=data.get("modules_per_line"),
            line_length=data.get("line_length"),
        )


@dataclass
class StructuralInformation:
    surface: Surface
    is_portrait: bool
    layouts: list[Layout]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            surface=Surface.from_dict(data.get("surface")),
            is_portrait=data.get("is_portrait"),
            layouts=[Layout.from_dict(layout) for layout in data.get("layouts")],
        )


@dataclass
class PvKitComponent:
    component: Component
    quantity: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            component=Component.from_dict(data.get("component")),
            quantity=data.get("quantity"),
        )


@dataclass
class PvKit(Summary):
    pv_kit_components: list[PvKitComponent]
    structural_informations: list[StructuralInformation] | None
    display_images: list[File]
    voltage: str
    phase: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            full_price=data.get("full_price"),
            final_price=data.get("final_price"),
            discount=data.get("discount"),
            power=data.get("power"),
            voltage=data.get("voltage"),
            phase=data.get("phase"),
            display_images=[
                File.from_dict(file) for file in data.get("display_images")
            ],
            structural_informations=[
                StructuralInformation.from_dict(structural_info)
                for structural_info in data.get("structural_informations", [])
            ],
            pv_kit_components=[
                PvKitComponent.from_dict(pv_kit_component)
                for pv_kit_component in data.get("pv_kit_components")
            ],
        )


@dataclass
class Order(Summary):
    pv_kits: list[PvKit]
    delivery_at: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            full_price=data.get("full_price"),
            final_price=data.get("final_price"),
            discount=data.get("discount"),
            power=data.get("power"),
            pv_kits=[PvKit.from_dict(pv_kit) for pv_kit in data.get("pv_kits")],
            delivery_at=data.get("shipping_info", {})
            .get("address", {})
            .get("brazilian_city", {})
            .get("name"),
        )
