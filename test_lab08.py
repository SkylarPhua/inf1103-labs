from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


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

#-------------------Test for Prediction 2---------------------
print("\n--- INVENTORY AGGREGATION TEST ---")

# physical_product already exists before either inventory is created.
inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(physical_product)

print(
    "Inventory A contains the original product:",
    inventory_a.find_product("P010") is physical_product,
)

inventory_a.remove_product("P010")

print(
    "\nInventory A lookup after removal:",
    inventory_a.find_product("P010"),
)

print("\nProduct still works after removal:")
physical_product.display_information()

inventory_b.add_product(physical_product)

print(
    "\nInventory B contains the same product object:",
    inventory_b.find_product("P010") is physical_product,
)