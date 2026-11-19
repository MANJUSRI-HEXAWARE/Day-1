transaction_ids = list(range(100001, 200001))
def linear_search(data, target):
    comparisons = 0
    for i in range(len(data)):
        comparisons += 1
        if data[i] == target:
            return i, comparisons
    return -1, comparisons
def binary_search(data, target):
    low = 0
    high = len(data) - 1
    comparisons = 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if data[mid] == target:
            return mid, comparisons
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons
n = len(transaction_ids)
print("=" * 65)
print("     BANK TRANSACTION SEARCHING SYSTEM")
print("=" * 65)
print("Total transaction IDs:", n)
print("First transaction ID:", transaction_ids[0])
print("Last transaction ID:", transaction_ids[-1])

linear_best_target = transaction_ids[0]
binary_best_target = transaction_ids[n // 2]

_, linear_best = linear_search(transaction_ids, linear_best_target)
_, binary_best = binary_search(transaction_ids, binary_best_target)

linear_average = (n + 1) / 2
total_binary_comparisons = 0

for target in transaction_ids:
    _, count = binary_search(transaction_ids, target)
    total_binary_comparisons += count

binary_average = total_binary_comparisons / n
worst_target = 200001
_, linear_worst = linear_search(transaction_ids, worst_target)
_, binary_worst = binary_search(transaction_ids, worst_target)
print("\nSEARCH COMPARISON RESULTS")
print("-" * 65)
print(f"{'Case':<15}{'Linear Search':<20}{'Binary Search':<20}")
print("-" * 65)
print(f"{'Best':<15}{linear_best:<20}{binary_best:<20}")
print(f"{'Average':<15}{linear_average:<20.2f}{binary_average:<20.2f}")
print(f"{'Worst':<15}{linear_worst:<20}{binary_worst:<20}")

search_id = 150075

print("\nTRANSACTION LOOKUP")
print("-" * 65)

index, comparisons = binary_search(transaction_ids, search_id)

if index != -1:
    print("Transaction ID found:", search_id)
    print("Position in dataset:", index)
    print("Comparisons required:", comparisons)
else:
    print("Transaction ID not found.")

print("=" * 65)
