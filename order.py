from product import Product
from order_line import OrderLine
from discount_strategy import DiscountStrategy
from no_discount import NoDiscount


class Order:
    def __init__(
        self,
        order_id: str,
        discount: DiscountStrategy | None = None,
    ) -> None:
        self.order_id: str = order_id
        self.__order_lines: list[OrderLine] = []
        self.discount: DiscountStrategy = NoDiscount() if discount is None else discount

    @property
    def order_lines(self) -> tuple[OrderLine, ...]:
        return tuple(self.__order_lines)

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, index: int) -> None:
        del self.__order_lines[index]

    def calculate_total(self) -> float:
        total = sum(
            (line.calculate_subtotal() for line in self.__order_lines),
            0.0,
        )
        return self.discount.apply(total)

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount