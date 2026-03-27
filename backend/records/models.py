from django.db import models

class MedicalRecord(models.Model):
    CONDITION_CHOICES = [
        ('FLU', 'Flu'),
        ('COLD', 'Common Cold'),
        ('ASTHMA', 'Asthma'),
        ('DIABETES', 'Diabetes'),
        ('HYPERTENSION', 'Hypertension'),
        ('COVID', 'COVID-19'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=50)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    doctor_notes = models.TextField(blank=True)
    date_of_visit = models.DateField(auto_now_add=True)
    date_of_exit = models.DateField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    next_appointment = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
