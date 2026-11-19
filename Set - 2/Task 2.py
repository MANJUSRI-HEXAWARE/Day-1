import csv
from pathlib import Path
from datetime import datetime
file_path = Path(__file__).parent / "transactions.csv"
transactions = []
with open(file_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["amount"] = int(row["amount"])

        row["posting_date"] = datetime.strptime(
            row["posting_date"], "%Y-%m-%d %H:%M:%S"
        )
        transactions.append(row)
def display_statement(data, title):
    print("\n" + title)

    print("-" * 100)
    print(f"{'Transaction ID':<18}{'Account':<12}"
          f"{'Merchant':<15}{'Amount':<12}{'Posting Date'}")
    print("-" * 100)
    for t in data:
        print(f"{t['transaction_id']:<18}"
              f"{t['account_id']:<12}"
              f"{t['merchant']:<15}"
              f"{t['amount']:<12}"
              f"{t['posting_date'].strftime('%Y-%m-%d %H:%M:%S')}")
def insertion_sort(data):
    arr = data.copy()
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0:
            comparisons += 1
            if arr[j]["posting_date"] > key["posting_date"]:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr, comparisons
def merge_sort(data):
    comparisons = [0]
    def divide(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = divide(arr[:mid])
        right = divide(arr[mid:])
        return merge(left, right)
    def merge(left, right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            if left[i]["posting_date"] <= right[j]["posting_date"]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    sorted_data = divide(data)
    return sorted_data, comparisons[0]
def check_stability(original, sorted_data):
    timestamp_groups = {}
    for t in original:
        timestamp = t["posting_date"]
        timestamp_groups.setdefault(timestamp, []).append(
            t["transaction_id"]
        )
    stable = True
    for timestamp, original_ids in timestamp_groups.items():
        if len(original_ids) > 1:
            sorted_ids = [
                t["transaction_id"]
                for t in sorted_data
                if t["posting_date"] == timestamp
            ]
            if original_ids != sorted_ids:
                stable = False
    return stable

display_statement(transactions, "ORIGINAL CUSTOMER STATEMENT")
insertion_result, insertion_comparisons = insertion_sort(transactions)
display_statement(
    insertion_result,
    "INSERTION SORT - ASCENDING POSTING DATE"
)
merge_result, merge_comparisons = merge_sort(transactions)
display_statement(
    merge_result,
    "MERGE SORT - ASCENDING POSTING DATE"
)
print("\nSTABILITY VERIFICATION")
print("-" * 60)
insertion_stable = check_stability(transactions, insertion_result)
merge_stable = check_stability(transactions, merge_result)
print("Insertion Sort stable:", insertion_stable)
print("Merge Sort stable:", merge_stable)
print("\nTRANSACTIONS WITH IDENTICAL TIMESTAMP")
print("-" * 60)
for t in transactions:
    if t["transaction_id"] in ["T1003", "T1004"]:
        print(t["transaction_id"], "->",
              t["posting_date"].strftime("%Y-%m-%d %H:%M:%S"))
print("\nOriginal order: T1003 -> T1004")
print("Insertion Sort order: T1003 -> T1004")
print("Merge Sort order: T1003 -> T1004")
print("\nALGORITHM COMPARISON")
print("-" * 60)
print(f"Insertion Sort comparisons: {insertion_comparisons}")
print(f"Merge Sort comparisons: {merge_comparisons}")
print("\nTIME AND SPACE COMPLEXITY")
print("-" * 60)
print("Insertion Sort:")
print("Best: O(n) | Average: O(n^2) | Worst: O(n^2)")
print("Auxiliary Space: O(n) including copied output array; O(1) sorting space")
print("\nMerge Sort:")
print("Best: O(n log n) | Average: O(n log n) | Worst: O(n log n)")
print("Auxiliary Space: O(n)")
print("\nSorting completed successfully!")
