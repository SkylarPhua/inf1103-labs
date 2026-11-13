from abc import ABC, abstractmethod
from supplier import Supplier


class Product(ABC):
    def __init__(
        self, product_id: str, name: str, price: float, stock: int, supplier: Supplier
    ) -> None:
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.supplier: Supplier = supplier

    @property
    def price(self) -> float:
        return self.__price

    def get_product_id(self):
        return self.__product_id

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        print(
            "ID:",
            self.__product_id,
            "| Name:",
            self.__name,
            "| Price: $" + format(self.__price, ".2f"),
            "| Stock:",
            self.__stock,
        )

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }

    @abstractmethod
    def get_fulfilment_info(self):
        pass
