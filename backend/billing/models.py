from django.db import models
from records.models import MedicalRecord


class Bill(models.Model):
    # Fixed: ForeignKey (not OneToOneField) — one patient can have multiple bills
    record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='bills')
    bill_number = models.CharField(max_length=20, unique=True)
    date_issued = models.DateField(auto_now_add=True)
    date_paid = models.DateField(null=True, blank=True)

    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    treatment_charges = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    medicine_charges = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    room_charges = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    lab_tests = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    other_charges = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        self.total_amount = (
            self.consultation_fee + self.treatment_charges +
            self.medicine_charges + self.room_charges +
            self.lab_tests + self.other_charges
        )
        if not self.bill_number:
            last = Bill.objects.order_by('-id').first()
            next_num = (last.id + 1) if last else 1
            self.bill_number = f'BILL-{str(next_num).zfill(3)}'
        super().save(*args, **kwargs)

    @property
    def is_paid(self):
        return self.date_paid is not None

    @property
    def patient_name(self):
        return self.record.name

    def __str__(self):
        return f"Bill #{self.bill_number} — {self.record.name}"
