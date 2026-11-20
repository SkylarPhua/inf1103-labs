import unittest

from digital_product import DigitalProduct
from physical_product import PhysicalProduct
from product_factory import ProductFactory
from supplier import Supplier


class ProductFactoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.supplier = Supplier(
            "S001", "Tech Supplier", "tech@example.com"
        )

    def test_creates_physical_product(self) -> None:
        product = ProductFactory.create(
            "physical",
            "P100",
            "Test Mouse",
            25.0,
            10,
            self.supplier,
            weight=0.15,
        )

        self.assertIsInstance(product, PhysicalProduct)
        self.assertIs(product.supplier, self.supplier)
        self.assertEqual(product.to_dict()["weight"], 0.15)

    def test_creates_digital_product(self) -> None:
        product = ProductFactory.create(
            "digital",
            "D100",
            "Test Software",
            50.0,
            5,
            self.supplier,
            download_size=500.0,
        )

        self.assertIsInstance(product, DigitalProduct)
        self.assertIs(product.supplier, self.supplier)
        self.assertEqual(
            product.to_dict()["download_size"], 500.0
        )

    def test_unknown_type_raises_value_error(self) -> None:
        with self.assertRaisesRegex(
            ValueError, "Unknown product type: service"
        ):
            ProductFactory.create(
                "service",
                "S100",
                "Installation",
                30.0,
                5,
                self.supplier,
            )


if __name__ == "__main__":
    unittest.main()