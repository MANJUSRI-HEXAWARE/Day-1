import csv
from pathlib import Path
DATA_FOLDER = Path(__file__).parent
booked_slots = set()
accepted_bookings = []
rejected_bookings = []
with open(DATA_FOLDER / "bookings.csv", "r", newline="") as file:
   reader = csv.DictReader(file)
   for booking in reader:
     booking_key = (
        booking["patient_id"],
        booking["slot"]
     )
     if booking_key in booked_slots:
        rejected_bookings.append(booking)
     else:
        booked_slots.add(booking_key)
        accepted_bookings.append(booking)
print("HOSPITAL DUPLICATE BOOKING DETECTION")
print("------------------------------------")
print("Total booking requests:", len(accepted_bookings) + len(rejected_bookings))
print("Accepted bookings:", len(accepted_bookings))
print("Rejected duplicate bookings:", len(rejected_bookings))
print("\nDuplicate Booking Details")
for booking in rejected_bookings:
  print(
     booking["booking_id"],
     "| Patient:", booking["patient_id"],
     "| Slot:", booking["slot"],
     "| Status: REJECTED"
  )
new_patient_id = "P100001"
new_slot = "09:00"
new_booking_key = (new_patient_id, new_slot)
print("\nNew Booking Validation")
if new_booking_key in booked_slots:
   print("Booking rejected: Patient already has an appointment in this slot.")
else:
   booked_slots.add(new_booking_key)
   print("Booking accepted: Slot is available for this patient.")
