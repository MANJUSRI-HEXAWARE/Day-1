import csv
from pathlib import Path
file_path = Path(__file__).parent / "transactions.csv"
transactions = []
with open(file_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        transactions.append({
            "id": row["transaction_id"],
            "amount": int(row["amount"])
        })
def brute_force(data):
    minimum = data[0]
    maximum = data[0]
    comparisons = 0
    for t in data[1:]:
        comparisons += 1
        if t["amount"] < minimum["amount"]:
            minimum = t
        comparisons += 1
        if t["amount"] > maximum["amount"]:
            maximum = t
    return minimum, maximum, comparisons
def divide_conquer(data):
    if len(data) == 1:
        return data[0], data[0], 0
    if len(data) == 2:
        comparisons = 1
        if data[0]["amount"] < data[1]["amount"]:
            return data[0], data[1], comparisons
        else:
            return data[1], data[0], comparisons
    mid = len(data) // 2
    left_min, left_max, left_count = divide_conquer(data[:mid])
    right_min, right_max, right_count = divide_conquer(data[mid:])
    comparisons = left_count + right_count
    comparisons += 1
    minimum = (
        left_min if left_min["amount"] < right_min["amount"]
        else right_min
    )
    comparisons += 1
    maximum = (
        left_max if left_max["amount"] > right_max["amount"]
        else right_max
    )
    return minimum, maximum, comparisons
bf_min, bf_max, bf_count = brute_force(transactions)
dc_min, dc_max, dc_count = divide_conquer(transactions)
print("\nTRANSACTION AMOUNT ANALYSIS")
print("-" * 45)
print("Total transactions:", len(transactions))
print("\nBRUTE FORCE")
print("Lowest Amount:", bf_min["amount"], "|", bf_min["id"])
print("Highest Amount:", bf_max["amount"], "|", bf_max["id"])
print("Comparisons:", bf_count)
print("\nDIVIDE AND CONQUER")
print("Lowest Amount:", dc_min["amount"], "|", dc_min["id"])
print("Highest Amount:", dc_max["amount"], "|", dc_max["id"])
print("Comparisons:", dc_count)
print("\nCOMPLEXITY COMPARISON")
print("Brute Force: O(n) time, O(1) auxiliary space")
print("Divide and Conquer: O(n) time, O(n) auxiliary space")
print("\nAnalysis completed.")
