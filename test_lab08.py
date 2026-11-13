from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order


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

#-------------------Test for Prediction 3---------------------
print("\n--- ORDER COMPOSITION TEST ---")

order_a = Order("O001")
order_b = Order("O002")

# Each order creates its own line for the same existing product.
order_a.add_order_line(physical_product, 2)
order_b.add_order_line(physical_product, 1)

print(
    "Both orders share the same Product:",
    order_a.order_lines[0].product is order_b.order_lines[0].product,
)

print(
    "Both orders share the same OrderLine:",
    order_a.order_lines[0] is order_b.order_lines[0],
)

print("\nOrder A: two OrderLines after adding the digital product")
order_a.add_order_line(digital_product, 3)

for line in order_a.order_lines:
    print(
        f"Product: {line.product.get_product_id()}"
        f" | Quantity: {line.quantity}"
        f" | Subtotal: ${line.calculate_subtotal():.2f}"
    )

print(f"Order A total: ${order_a.calculate_total():.2f}")

# Index 0 is Order A's physical-product line.
order_a.remove_order_line(0)

print("\nAfter removing Order A's first line:")
print("Order A line count:", len(order_a.order_lines))
print(f"Order A total: ${order_a.calculate_total():.2f}")
print("Order B line count:", len(order_b.order_lines))

print("\nThe referenced Product still works:")
physical_product.display_information()