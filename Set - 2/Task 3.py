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

transaction_groups = {}
for t in transactions:
    key = (t["account_id"], t["amount"], t["merchant"])

    if key not in transaction_groups:
        transaction_groups[key] = []
    transaction_groups[key].append(t)
duplicates = []
for key, group in transaction_groups.items():
    group.sort(key=lambda x: x["posting_date"])
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            time_difference = (
                group[j]["posting_date"] - group[i]["posting_date"]
            ).total_seconds()
            if time_difference <= 60:
                duplicates.append(
                    (group[i], group[j], int(time_difference))
                )
            else:
                break

print("\nDUPLICATE TRANSACTION DETECTION")
print("-" * 65)
print("Total transactions:", len(transactions))
print("Duplicate pairs found:", len(duplicates))

for first, second, seconds in duplicates:
    print("\nDuplicate Transactions:")
    print("Transaction 1:", first["transaction_id"])
    print("Transaction 2:", second["transaction_id"])
    print("Account ID:", first["account_id"])
    print("Merchant:", first["merchant"])
    print("Amount: Rs.", first["amount"])
    print("Time Difference:", seconds, "seconds")
    print("Status: POSSIBLE DUPLICATE")
print("\nDetection completed.")
