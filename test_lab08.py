from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


supplier = Supplier(
    "S001",
    "Tech Supplier",
    "tech@example.com",
)

physical_product = PhysicalProduct(
    "P010",
    "Gaming Mouse",
    120.00,
    10,
    0.15,
    supplier,
)

digital_product = DigitalProduct(
    "P011",
    "Antivirus Software",
    59.90,
    2,
    500.0,
    supplier,
)

print("Before deleting the supplier variable:")
physical_product.supplier.display_information()
digital_product.supplier.display_information()

del supplier

print("\nAfter deleting the supplier variable:")
physical_product.supplier.display_information()
digital_product.supplier.display_information()

print(
    "\nBoth products reference the same supplier:",
    physical_product.supplier is digital_product.supplier,
)