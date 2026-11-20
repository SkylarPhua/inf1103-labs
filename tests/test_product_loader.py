import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from inventory import Inventory
from product_loader import load_products
from supplier import Supplier


class ProductLoaderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.inventory = Inventory()
        self.supplier = Supplier(
            "S001", "Tech Supplier", "tech@example.com"
        )

    def test_skips_bad_rows_and_loads_valid_products(self) -> None:
        path = (
            Path(__file__).resolve().parent.parent
            / "products.csv"
        )
        output = io.StringIO()

        with redirect_stdout(output):
            load_products(
                str(path), self.inventory, self.supplier
            )

        self.assertEqual(len(self.inventory.get_products()), 3)

        for product_id in ("P001", "D001", "P003"):
            with self.subTest(product_id=product_id):
                product = self.inventory.find_product(product_id)
                self.assertIsNotNone(product)
                self.assertIs(product.supplier, self.supplier)

        self.assertIsNone(self.inventory.find_product("S001"))
        self.assertIsNone(self.inventory.find_product("P002"))

        self.assertEqual(
            output.getvalue().splitlines(),
            [
                "Skipping row 4: Unknown product type: service",
                "Skipping row 5: could not convert string to float: 'abc'",
                "3 products loaded.",
                "Load attempt finished.",
            ],
        )

    def test_missing_file_is_handled(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            path = str(Path(folder) / "missing.csv")
            output = io.StringIO()

            with redirect_stdout(output):
                load_products(
                    path, self.inventory, self.supplier
                )

            self.assertEqual(
                output.getvalue().splitlines(),
                [
                    f"Products file not found: {path}",
                    "Load attempt finished.",
                ],
            )
            self.assertEqual(
                len(self.inventory.get_products()), 0
            )


if __name__ == "__main__":
    unittest.main()