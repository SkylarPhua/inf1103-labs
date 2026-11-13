from abc import ABC, abstractmethod
from supplier import Supplier


class Product(ABC):
    def __init__(
        self, product_id: str, name: str, price: float, stock: int, supplier: Supplier
    ) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.supplier: Supplier = supplier

    @property
    def price(self) -> float:
        return self.__price

    def get_product_id(self) -> str:
        return self.__product_id

    def update_stock(self, quantity: int) -> None:
        self.__stock = quantity

    def display_information(self) -> None:
        print(
            "ID:",
            self.__product_id,
            "| Name:",
            self.__name,
            "| Price: $" + format(self.__price, ".2f"),
            "| Stock:",
            self.__stock,
        )
        self.supplier.display_information()

    def to_dict(self) -> dict[str, str | float | int | dict[str, str]]:
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.supplier.to_dict(),
        }

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass
