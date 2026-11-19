import csv 
import time 
from pathlib import Path 
FILE_PATH = Path(__file__).resolve().parent / "orders.csv" 
def load_orders(): 
    orders = [] 
    with open(FILE_PATH, "r", newline="", encoding="utf-8") as file: 
        reader = csv.DictReader(file) 
        for row in reader: 
            row["amount"] = int(row["amount"]) 
            orders.append(row) 
    return orders 
def linear_search(orders, target): 
    comparisons = 0 
    for order in orders: 
        comparisons += 1 
        if order["orderId"] == target: 
            return order, comparisons 
    return None, comparisons 
def binary_search(orders, target): 
    low = 0 
    high = len(orders) - 1 
    comparisons = 0 
    while low <= high: 
        mid = (low + high) // 2 
        comparisons += 1 
        if orders[mid]["orderId"] == target: 
            return orders[mid], comparisons 
        elif orders[mid]["orderId"] < target: 
            low = mid + 1 
        else: 
            high = mid - 1 
    return None, comparisons 
def display_order(order): 
    if order is None: 
        print("Order not found!") 
    else: 
        print("Order ID    :", order["orderId"]) 
        print("Customer ID :", order["customerId"]) 
        print("Amount      : Rs.", order["amount"]) 
        print("Created At  :", order["createdAt"]) 
def main(): 
    print("=" * 60) 
    print("TASK 1 - ORDER SEARCHING SYSTEM") 
    print("=" * 60) 
    orders = load_orders() 
    print("\nDATASET INFORMATION") 
    print("-" * 60) 
    print("Total Orders Loaded:", len(orders)) 
    print("CSV File:", FILE_PATH.name) 
    target = input("\nEnter Order ID (Example: ORD050000): 
").strip().upper() 
    print("\n" + "=" * 60) 
    print("LINEAR SEARCH RESULT") 
    print("=" * 60) 
    start = time.perf_counter() 
    linear_result, linear_comparisons = linear_search(orders, target) 
    linear_time = time.perf_counter() - start 
    display_order(linear_result) 
    print("Comparisons :", linear_comparisons) 
    print("Search Time :", f"{linear_time:.8f}", "seconds") 
    sorted_orders = sorted(orders, key=lambda order: 
order["orderId"]) 
    print("\n" + "=" * 60) 
    print("BINARY SEARCH RESULT") 
    print("=" * 60) 
    start = time.perf_counter() 
    binary_result, binary_comparisons = 
binary_search(sorted_orders, target) 
    binary_time = time.perf_counter() - start 
    display_order(binary_result) 
    print("Comparisons :", binary_comparisons) 
    print("Search Time :", f"{binary_time:.8f}", "seconds") 
    print("\n" + "=" * 60) 
    print("BENCHMARK COMPARISON - 50,000 RECORDS") 
    print("=" * 60) 
    print(f"{'Algorithm':<20}{'Comparisons':<18}{'Time (seconds)'}") 
    print("-" * 60) 
    print(f"{'Linear 
Search':<20}{linear_comparisons:<18}{linear_time:.8f}") 
    print(f"{'Binary 
Search':<20}{binary_comparisons:<18}{binary_time:.8f}") 
    print("-" * 60) 
    if linear_result == binary_result: 
        print("Verification: Both searches returned the same result.") 
    else: 
        print("Verification: Search results do not match!") 
    print("\nTASK 1 EXECUTION COMPLETED") 
if __name__ == "__main__": 
    main()
