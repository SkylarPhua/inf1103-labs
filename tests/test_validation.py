import unittest

from order import Order
from product_factory import ProductFactory
from supplier import Supplier


class ValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.supplier = Supplier(
            "S001", "Tech Supplier", "tech@example.com"
        )

    def test_rejects_zero_and_negative_prices(self) -> None:
        for product_type in ("physical", "digital"):
            for price in (0.0, -5.0):
                with self.subTest(
                    product_type=product_type, price=price
                ):
                    with self.assertRaisesRegex(
                        ValueError,
                        "Price must be greater than zero",
                    ):
                        ProductFactory.create(
                            product_type,
                            "P100",
                            "Test Product",
                            price,
                            10,
                            self.supplier,
                        )

    def test_rejects_negative_initial_stock(self) -> None:
        for product_type in ("physical", "digital"):
            with self.subTest(product_type=product_type):
                with self.assertRaisesRegex(
                    ValueError,
                    "Stock quantity cannot be negative",
                ):
                    ProductFactory.create(
                        product_type,
                        "P100",
                        "Test Product",
                        25.0,
                        -1,
                        self.supplier,
                    )

    def test_stock_updates_preserve_the_rule(self) -> None:
        for product_type in ("physical", "digital"):
            with self.subTest(product_type=product_type):
                product = ProductFactory.create(
                    product_type,
                    "P100",
                    "Test Product",
                    25.0,
                    10,
                    self.supplier,
                )

                with self.assertRaises(ValueError):
                    product.update_stock(-1)

                self.assertEqual(product.to_dict()["stock"], 10)

                product.update_stock(0)
                self.assertEqual(product.to_dict()["stock"], 0)

    def test_rejects_zero_and_negative_order_quantities(self) -> None:
        product = ProductFactory.create(
            "physical",
            "P100",
            "Test Product",
            25.0,
            10,
            self.supplier,
        )
        order = Order("O100")

        for quantity in (0, -1):
            with self.subTest(quantity=quantity):
                with self.assertRaisesRegex(
                    ValueError,
                    "Quantity must be greater than zero",
                ):
                    order.add_order_line(product, quantity)

        self.assertEqual(len(order.order_lines), 0)

        order.add_order_line(product, 2)
        self.assertEqual(order.calculate_total(), 50.0)


if __name__ == "__main__":
    unittest.main()