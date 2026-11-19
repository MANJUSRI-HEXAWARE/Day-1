import csv
import random
import time
from pathlib import Path
DATA_FOLDER = Path(__file__).parent
with open(DATA_FOLDER / "patients.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    patients = list(reader)

patients.sort(key=lambda patient: patient["patient_id"])
patient_ids = [patient["patient_id"] for patient in patients]

random.seed(42)
search_requests = random.choices(patient_ids, k=1000)
def linear_search(records, target):
    comparisons = 0
    for patient in records:
        comparisons += 1
        if patient["patient_id"] == target:
            return patient, comparisons
    return None, comparisons

def binary_search(records, target):
    low = 0
    high = len(records) - 1
    comparisons = 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if records[mid]["patient_id"] == target:
            return records[mid], comparisons
        elif records[mid]["patient_id"] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None, comparisons

linear_total_comparisons = 0
start_time = time.perf_counter()
for patient_id in search_requests:
    result, count = linear_search(patients, patient_id)
    linear_total_comparisons += count
    if result is None:
        raise RuntimeError("Patient record not found.")

linear_time = time.perf_counter() - start_time
binary_total_comparisons = 0
start_time = time.perf_counter()
for patient_id in search_requests:
    result, count = binary_search(patients, patient_id)
    binary_total_comparisons += count
    if result is None:
        raise RuntimeError("Patient record not found.")

binary_time = time.perf_counter() - start_time
print("HOSPITAL PATIENT SEARCH ANALYSIS")
print("--------------------------------")
print("Total patient records:", len(patients))
print("Total lookup requests:", len(search_requests))
print()
print("Linear Search")
print("Total comparisons:", linear_total_comparisons)
print("Average comparisons:", round(linear_total_comparisons /
1000, 2))
print("Execution time:", round(linear_time, 6), "seconds")
print()
print("Binary Search")
print("Total comparisons:", binary_total_comparisons)
print("Average comparisons:", round(binary_total_comparisons /
1000, 2))
print("Execution time:", round(binary_time, 6), "seconds")
