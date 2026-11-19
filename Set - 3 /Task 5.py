import csv
from pathlib import Path
from bisect import bisect_right
DATA_FOLDER = Path(__file__).parent
def to_minutes(time_text):
    hours, minutes = map(int, time_text.split(":"))
    return hours * 60 + minutes
def format_time(minutes):
    return f"{minutes // 60:02d}:{minutes % 60:02d}"
with open(DATA_FOLDER / "appointments.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    appointments = [
        row for row in reader
        if row["doctor_id"] == "D01"
    ]
for appointment in appointments:
    appointment["start"] = to_minutes(appointment["start_time"])
    appointment["end"] = to_minutes(appointment["end_time"])
appointments.sort(key=lambda a: (a["end"], a["start"]))
n = len(appointments)
finish_times = [a["end"] for a in appointments]
predecessor = []
for i in range(n):
    p = bisect_right(finish_times, appointments[i]["start"], 0, i) - 1
    predecessor.append(p)
dp = [0] * (n + 1)
for i in range(1, n + 1):
    include = 1 + dp[predecessor[i - 1] + 1]
    exclude = dp[i - 1]
    dp[i] = max(include, exclude)
selected_dp = []
i = n
while i > 0:
    appointment = appointments[i - 1]
    include = 1 + dp[predecessor[i - 1] + 1]
    if include > dp[i - 1]:
        selected_dp.append(appointment)
        i = predecessor[i - 1] + 1
    else:
        i -= 1
selected_dp.reverse()
selected_greedy = []
last_finish = -1
for appointment in appointments:
    if appointment["start"] >= last_finish:
        selected_greedy.append(appointment)
        last_finish = appointment["end"]
print("DOCTOR APPOINTMENT SCHEDULING")
print("-----------------------------")
print("Doctor ID: D01")
print("Total appointment requests:", n)
print("\nDynamic Programming")
print("Maximum appointments:", dp[n])
print("Selected schedule:")
for appointment in selected_dp:
    print(
        appointment["appointment_id"],
        "|",
        format_time(appointment["start"]),
        "-",
        format_time(appointment["end"])
    )
print("\nGreedy Approach")
print("Appointments selected:", len(selected_greedy))
for appointment in selected_greedy:
    print(
        appointment["appointment_id"],
        "|",
        format_time(appointment["start"]),
        "-",
        format_time(appointment["end"])
    )
print("\nComparison")
if len(selected_dp) == len(selected_greedy):
    print("DP and Greedy results: PASSED")
    print("Both approaches selected the maximum number of appointments.")
else:
    print("DP and Greedy results: FAILED")
