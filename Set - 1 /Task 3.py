
import csv
from datetime import datetime
from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent / "orders.csv"

def load_orders():
    with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

def find_duplicates(orders):
    seen = {}
    duplicates = []

    for order in orders:
        customer_id = order["customerId"]
        amount = float(order["amount"])

        created_at = datetime.strptime(
            order["createdAt"],
            "%Y-%m-%d %H:%M:%S"
        )

        minute = created_at.strftime("%Y-%m-%d %H:%M")
        key = (customer_id, amount, minute)

        if key in seen:
            duplicates.append({
                "original": seen[key],
                "duplicate": order,
                "minute": minute
            })
        else:
            seen[key] = order

    return duplicates


def main():
    print("=" * 70)
    print("TASK 3 - DUPLICATE ORDER DETECTION")
    print("=" * 70)

    orders = load_orders()

    print("\nDATASET INFORMATION")
    print("-" * 70)
    print("Total orders loaded:", len(orders))

    duplicates = find_duplicates(orders)

    print("\nDUPLICATE ORDER DETAILS")
    print("-" * 70)

    if duplicates:
        for i, item in enumerate(duplicates, start=1):
            original = item["original"]
            duplicate = item["duplicate"]

            print(f"\nDuplicate {i}")
            print("Original Order ID :", original["orderId"])
            print("Duplicate Order ID:", duplicate["orderId"])
            print("Customer ID       :", duplicate["customerId"])
            print("Order Amount : Rs.", duplicate["amount"])
            print("Created Minute :", item["minute"])
    else:
        print("No duplicate orders found.")

    print("\n" + "=" * 70)
    print("DUPLICATE DETECTION SUMMARY")
    print("=" * 70)
    print("Total Orders     :", len(orders))
    print("Duplicate Orders :", len(duplicates))
    print("Unique First Entries:", len(orders) - len(duplicates))
    print("\nTASK 3 EXECUTION COMPLETED")


if __name__ == "__main__":
    main()
