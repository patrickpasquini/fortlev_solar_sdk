from dataclasses import dataclass


@dataclass
class Installment:
    """Represents a financing installment.

    Attributes:
        value (float): The value of the installment.
        quantity (int): The number of installments.
        entry_value (float): The entry value to be paid upfront.

    Methods:
        from_dict(data: dict): Creates an Installment instance from a dictionary.
    """

    value: float
    quantity: int
    entry_value: float

    @classmethod
    def from_dict(cls, data: dict) -> "Installment":
        """Creates an Installment instance from a dictionary.

        Args:
            data (dict): A dictionary containing installment details.

        Returns:
            Installment: An instance of Installment populated with data from the dictionary.
        """
        return cls(
            value=data.get("value"),
            quantity=data.get("quantity"),
            entry_value=data.get("entry_value"),
        )


@dataclass
class Financing:
    """Represents financing information provided by a bank.

    Attributes:
        bank (str): The name of the bank providing the financing.
        installments (list[Installment]): A list of Installment instances representing the financing terms.

    Methods:
        from_dict(data: dict): Creates a Financing instance from a dictionary.
    """

    bank: str
    installments: list[Installment]

    @classmethod
    def from_dict(cls, data: dict) -> "Financing":
        """
        Creates a Financing instance from a dictionary.

        Args:
            data (dict): A dictionary containing component details.

        Returns:
            Financing: A new Financing instance with attributes populated from the dictionary.
        """
        return cls(
            bank=data.get("bank", {}).get("name"),
            installments=[
                Installment.from_dict(installment)
                for installment in data.get("installments")
            ],
        )
