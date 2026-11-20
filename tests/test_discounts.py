import unittest

from bulk_discount import BulkDiscount
from no_discount import NoDiscount
from order import Order
from percentage_discount import PercentageDiscount
from physical_product import PhysicalProduct
from supplier import Supplier
from student_discount import StudentDiscount


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
        supplier = Supplier("S001", "Tech Supplier", "tech@example.com")
        product = PhysicalProduct("P100", "Test Product", 125.0, 10, 1.0, supplier)

        order = Order("O100")
        order.add_order_line(product, 2)
        return order

    def test_student_discount_without_changing_order(self) -> None:
        order = self.make_order()
        order.set_discount(StudentDiscount())

        self.assertAlmostEqual(order.calculate_total(), 237.50)

    def test_orders_can_share_a_discount_strategy(self) -> None:
        shared_discount = PercentageDiscount(10)

        order_a = self.make_order()
        order_b = Order("O200")

        order_a.set_discount(shared_discount)
        order_b.set_discount(shared_discount)

        self.assertIs(order_a.discount, order_b.discount)
        self.assertAlmostEqual(order_a.calculate_total(), 225.0)

        # Changing Order A's reference does not change Order B's.
        order_a.set_discount(NoDiscount())

        self.assertEqual(order_a.calculate_total(), 250.0)
        self.assertIs(order_b.discount, shared_discount)


if __name__ == "__main__":
    unittest.main()
