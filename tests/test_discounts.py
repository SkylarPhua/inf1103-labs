import unittest

from bulk_discount import BulkDiscount
from no_discount import NoDiscount
from order import Order
from percentage_discount import PercentageDiscount
from physical_product import PhysicalProduct
from supplier import Supplier


class DiscountTests(unittest.TestCase):
    def test_no_discount(self) -> None:
        self.assertEqual(NoDiscount().apply(250.0), 250.0)

    def test_percentage_discount(self) -> None:
        self.assertAlmostEqual(
            PercentageDiscount(10).apply(250.0),
            225.0,
        )

    def test_bulk_discount_threshold(self) -> None:
        discount = BulkDiscount(200, 20)

        self.assertEqual(discount.apply(199.0), 199.0)
        self.assertEqual(discount.apply(200.0), 180.0)
        self.assertEqual(discount.apply(250.0), 230.0)

    def test_order_uses_no_discount_by_default(self) -> None:
        order = self.make_order()

        self.assertEqual(order.calculate_total(), 250.0)

    def test_order_can_switch_discount(self) -> None:
        order = self.make_order()
        order.set_discount(BulkDiscount(200, 20))

        self.assertEqual(order.calculate_total(), 230.0)

        order.set_discount(PercentageDiscount(10))

        self.assertAlmostEqual(order.calculate_total(), 225.0)

    def make_order(self) -> Order:
        supplier = Supplier(
            "S001", "Tech Supplier", "tech@example.com"
        )
        product = PhysicalProduct(
            "P100", "Test Product", 125.0, 10, 1.0, supplier
        )

        order = Order("O100")
        order.add_order_line(product, 2)
        return order


if __name__ == "__main__":
    unittest.main()