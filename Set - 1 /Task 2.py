
import csv
import time
from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent / "orders.csv"


def load_orders():
    with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        orders = list(reader)

    for order in orders:
        order["amount"] = int(order["amount"])

    return orders


def selection_sort(orders):
    arr = orders.copy()
    n = len(arr)

    for i in range(n - 1):
        max_index = i

        for j in range(i + 1, n):
            if arr[j]["amount"] > arr[max_index]["amount"]:
                max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


def merge_sort(orders):
    if len(orders) <= 1:
        return orders.copy()

    mid = len(orders) // 2

    left = merge_sort(orders[:mid])
    right = merge_sort(orders[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["amount"] >= right[j]["amount"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def display_top_orders(orders):
    print(f"{'Order ID':<15}{'Customer ID':<18}{'Amount':>10}")
    print("-" * 45)

    for order in orders[:5]:
        print(
            f"{order['orderId']:<15}"
            f"{order['customerId']:<18}"
            f"{order['amount']:>10}"
        )


def show_passes():
    arr = [2500, 1500, 4500, 800, 6000]

    print("\nFIRST THREE PASSES - SELECTION SORT")
    print("Initial List:", arr)

    for i in range(3):
        max_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]

        print(f"Pass {i + 1}:", arr)


def main():
    print("=" * 65)
    print("TASK 2 - ORDER SORTING SYSTEM")
    print("=" * 65)

    orders = load_orders()
    orders = orders[:10000]

    print("\nDATASET INFORMATION")
    print("-" * 65)
    print("Total records loaded:", len(orders))
    print("Sorting field: Amount")
    print("Sorting order: Descending")

    show_passes()

    print("\n" + "=" * 65)
    print("SELECTION SORT - O(n^2)")
    print("=" * 65)

    start = time.perf_counter()
    selection_result = selection_sort(orders)
    selection_time = time.perf_counter() - start

    display_top_orders(selection_result)

    print("\nExecution Time:", f"{selection_time:.6f}", "seconds")

    print("\n" + "=" * 65)
    print("MERGE SORT - O(n log n)")
    print("=" * 65)

    start = time.perf_counter()
    merge_result = merge_sort(orders)
    merge_time = time.perf_counter() - start

    display_top_orders(merge_result)

    print("\nExecution Time:", f"{merge_time:.6f}", "seconds")

    print("\n" + "=" * 65)
    print("PYTHON BUILT-IN SORT")
    print("=" * 65)

    start = time.perf_counter()

    builtin_result = sorted(
        orders,
        key=lambda order: order["amount"],
        reverse=True
    )

    builtin_time = time.perf_counter() - start

    display_top_orders(builtin_result)

    print("\nExecution Time:", f"{builtin_time:.6f}", "seconds")

    print("\n" + "=" * 65)
    print("SORTING BENCHMARK - 10,000 RECORDS")
    print("=" * 65)

    print(f"{'Algorithm':<22}{'Time (seconds)':>20}")
    print("-" * 45)

    print(f"{'Selection Sort':<22}{selection_time:>20.6f}")
    print(f"{'Merge Sort':<22}{merge_time:>20.6f}")
    print(f"{'Built-in Sort':<22}{builtin_time:>20.6f}")

    print("-" * 45)

    selection_amounts = [x["amount"] for x in selection_result]
    merge_amounts = [x["amount"] for x in merge_result]
    builtin_amounts = [x["amount"] for x in builtin_result]

    correct = (
        selection_amounts == merge_amounts == builtin_amounts
        and all(
            builtin_amounts[i] >= builtin_amounts[i + 1]
            for i in range(len(builtin_amounts) - 1)
        )
    )

    print("\nVERIFICATION")

    if correct:
        print("All three sorting algorithms produced the correct result.")
        print("Orders are arranged in descending order.")
    else:
        print("Sorting verification failed.")

    print("\nTASK 2 EXECUTION COMPLETED")


if __name__ == "__main__":
    main()
