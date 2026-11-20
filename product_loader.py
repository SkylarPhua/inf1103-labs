import csv

from inventory import Inventory
from product_factory import ProductFactory
from supplier import Supplier


def load_products(
    path: str,
    inventory: Inventory,
    supplier: Supplier,
) -> None:
    try:
        file = open(path, newline="", encoding="utf-8")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    else:
        loaded = 0

        with file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header.

            for row_number, row in enumerate(reader, start=2):
                try:
                    (
                        product_type,
                        product_id,
                        name,
                        price_text,
                        stock_text,
                    ) = row

                    product = ProductFactory.create(
                        product_type,
                        product_id,
                        name,
                        float(price_text),
                        int(stock_text),
                        supplier,
                    )

                    inventory.add_product(product)
                    loaded += 1

                except ValueError as error:
                    print(f"Skipping row {row_number}: {error}")

        print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished.")