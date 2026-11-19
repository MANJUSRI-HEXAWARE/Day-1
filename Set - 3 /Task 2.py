import csv
import time
from pathlib import Path
DATA_FOLDER = Path(__file__).parent
URGENCY_RANK = {
    "Critical": 1,
    "High": 2,
    "Medium": 3,
    "Low": 4
}
def appointment_key(appointment):
    return (
        URGENCY_RANK[appointment["urgency"]],
        appointment["arrival_time"]
    )
def selection_sort(records):
    arr = records.copy()
    swaps = 0
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if appointment_key(arr[j]) < appointment_key(arr[min_index]):
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    return arr, swaps

def quick_sort(records):
    arr = records.copy()
    swaps = 0
    def partition(low, high):
        nonlocal swaps
        pivot = appointment_key(arr[high])
        i = low - 1
        for j in range(low, high):
            if appointment_key(arr[j]) <= pivot:
                i += 1
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1
        if i + 1 != high:
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            swaps += 1
        return i + 1
    def sort(low, high):
        if low < high:
            pivot_index = partition(low, high)
            sort(low, pivot_index - 1)
            sort(pivot_index + 1, high)
    sort(0, len(arr) - 1)
    return arr, swaps
with open(DATA_FOLDER / "appointments.csv", "r", newline="") as file:
    appointments = list(csv.DictReader(file))
start = time.perf_counter()
selection_result, selection_swaps = selection_sort(appointments)
selection_time = time.perf_counter() - start
start = time.perf_counter()
quick_result, quick_swaps = quick_sort(appointments)
quick_time = time.perf_counter() - start
selection_keys = [appointment_key(a) for a in selection_result]
quick_keys = [appointment_key(a) for a in quick_result]
if selection_keys != quick_keys:
    raise RuntimeError("Sorting results do not match.")
print("HOSPITAL APPOINTMENT PRIORITIZATION")
print("-----------------------------------")
print("Total appointments:", len(appointments))
print()
print("Selection Sort")
print("Swaps:", selection_swaps)
print("Execution time:", round(selection_time, 8), "seconds")
print()
print("Quick Sort")
print("Swaps:", quick_swaps)
print("Execution time:", round(quick_time, 8), "seconds")
print()
print("Sorted Appointments")
for appointment in selection_result:
    print(
        appointment["appointment_id"],
        "| Patient:", appointment["patient_id"],
        "| Urgency:", appointment["urgency"],
        "| Arrival:", appointment["arrival_time"]
    )
print()
print("Sorting verification: PASSED")
