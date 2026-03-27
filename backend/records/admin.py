from django.contrib import admin
from .models import MedicalRecord

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'condition', 'date_of_visit', 'date_of_exit', 'next_appointment')
    list_filter = ('condition',)
    search_fields = ('name', 'doctor_notes')
