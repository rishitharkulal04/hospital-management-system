"""
Run this ONCE after migrating to seed demo data:
    python seed.py
"""
import os, django, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from records.models import MedicalRecord
from billing.models import Bill
from datetime import date

print("Seeding records...")
patients = [
    MedicalRecord(name='Rahul Sharma', condition='DIABETES', doctor_notes='Blood sugar stable, continue metformin.', date_of_exit=date(2025,3,5), next_appointment=date(2025,4,1)),
    MedicalRecord(name='Priya Iyer', condition='FLU', doctor_notes='Mild fever, prescribed paracetamol.', date_of_exit=date(2025,3,4), next_appointment=date(2025,3,20)),
    MedicalRecord(name='Anil Kumar', condition='HYPERTENSION', doctor_notes='BP 150/90, adjust medication.', date_of_exit=None, next_appointment=date(2025,3,15)),
    MedicalRecord(name='Sunita Rao', condition='ASTHMA', doctor_notes='Inhaler usage increased. Monitor.', date_of_exit=date(2025,3,7), next_appointment=date(2025,4,5)),
    MedicalRecord(name='Vikram Singh', condition='COVID', doctor_notes='Mild symptoms, isolation advised.', date_of_exit=None, next_appointment=None),
    MedicalRecord(name='Deepa Nair', condition='COLD', doctor_notes='Prescribed antihistamines.', date_of_exit=date(2025,3,8), next_appointment=None),
    MedicalRecord(name='Ravi Pillai', condition='OTHER', doctor_notes='Routine checkup. All clear.', date_of_exit=date(2025,3,2), next_appointment=date(2025,9,1)),
]
for p in patients:
    p.save()
print(f"  Created {len(patients)} patients")

print("Seeding bills...")
p = {r.name: r for r in MedicalRecord.objects.all()}
bills_data = [
    dict(record=p['Rahul Sharma'], bill_number='BILL-001', consultation_fee=500, treatment_charges=2000, medicine_charges=800, room_charges=3000, lab_tests=1200, date_paid=date(2025,3,6)),
    dict(record=p['Priya Iyer'], bill_number='BILL-002', consultation_fee=500, medicine_charges=350, lab_tests=400),
    dict(record=p['Sunita Rao'], bill_number='BILL-003', consultation_fee=500, treatment_charges=1500, medicine_charges=600, room_charges=4000, lab_tests=800, other_charges=200),
    dict(record=p['Deepa Nair'], bill_number='BILL-004', consultation_fee=500, medicine_charges=200, date_paid=date(2025,3,8)),
]
for bd in bills_data:
    Bill(**bd).save()
print(f"  Created {len(bills_data)} bills")
print("Done! ✓")
