from dataclasses import dataclass
from .base_classes import Summary, File
from .surface import Surface
from .component import Component


@dataclass
class Layout:
    """
    Represents the layout configuration for solar modules in a PV kit.

    Attributes:
        line_quantity (int): The number of lines in the layout.
        modules_per_line (int): The number of modules per line in the layout.
        line_length (float): The length of each line in the layout.
    """

    line_quantity: int
    modules_per_line: int
    line_length: float

    @classmethod
    def from_dict(cls, data: dict) -> "Layout":
        """
        Creates an instance of Layout from a dictionary.

        Args:
            data (dict): A dictionary containing layout information.

        Returns:
            Layout: An instance of the Layout class.
        """
        return cls(
            line_quantity=data.get("line_quantity"),
            modules_per_line=data.get("modules_per_line"),
            line_length=data.get("line_length"),
        )


@dataclass
class StructuralInformation:
    """
    Represents the structural information related to a PV kit installation.

    Attributes:
        surface (Surface): The surface where the PV kit is installed.
        is_portrait (bool): Indicates if the modules are installed in portrait orientation.
        layouts (list[Layout]): A list of layout configurations.
    """

    surface: Surface
    is_portrait: bool
    layouts: list[Layout]

    @classmethod
    def from_dict(cls, data: dict) -> "StructuralInformation":
        """
        Creates an instance of StructuralInformation from a dictionary.

        Args:
            data (dict): A dictionary containing structural information.

        Returns:
            StructuralInformation: An instance of the StructuralInformation class.
        """
        return cls(
            surface=Surface.from_dict(data.get("surface")),
            is_portrait=data.get("is_portrait"),
            layouts=[Layout.from_dict(layout) for layout in data.get("layouts")],
        )


@dataclass
class PvKitComponent:
    """
    Represents a component used in a PV kit and its quantity.

    Attributes:
        component (Component): The component included in the PV kit.
        quantity (int): The quantity of the component used in the PV kit.
    """

    component: Component
    quantity: int

    @classmethod
    def from_dict(cls, data: dict) -> "PvKit":
        """
        Creates an instance of PvKitComponent from a dictionary.

        Args:
            data (dict): A dictionary containing component information.

        Returns:
            PvKitComponent: An instance of the PvKitComponent class.
        """
        return cls(
            component=Component.from_dict(data.get("component")),
            quantity=data.get("quantity"),
        )


@dataclass
class PvKit(Summary):
    """
    Represents a PV kit, which includes components, structural information, and other attributes.

    Inherits from:
        Summary: Provides attributes such as full_price, final_price, discount, and power.

    Attributes:
        pv_kit_components (list[PvKitComponent]): A list of components included in the PV kit.
        structural_informations (list[StructuralInformation] | None): Structural details of the PV kit.
        display_images (list[File]): A list of image files for displaying the PV kit.
        voltage (str): The voltage rating of the PV kit.
        phase (int): The phase configuration of the PV kit.
    """

    pv_kit_components: list[PvKitComponent]
    structural_informations: list[StructuralInformation] | None
    display_images: list[File]
    voltage: str
    phase: int

    @classmethod
    def from_dict(cls, data: dict) -> "PvKit":
        """
        Creates an instance of PvKit from a dictionary.

        Args:
            data (dict): A dictionary containing PV kit information.

        Returns:
            PvKit: An instance of the PvKit class.
        """
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
    """
    Represents an order containing multiple PV kits and delivery information.

    Inherits from:
        Summary: Provides attributes such as full_price, final_price, discount, and power.

    Attributes:
        pv_kits (list[PvKit]): A list of PV kits included in the order.
        delivery_at (str): The delivery location or city for the order.
    """

    pv_kits: list[PvKit]
    delivery_at: str

    @classmethod
    def from_dict(cls, data: dict) -> "Order":
        """
        Creates an instance of Order from a dictionary.

        Args:
            data (dict): A dictionary containing order information.

        Returns:
            Order: An instance of the Order class.
        """
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
