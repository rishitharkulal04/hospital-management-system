from rest_framework import serializers
from .models import Bill
from records.serializers import MedicalRecordSerializer


class BillSerializer(serializers.ModelSerializer):
    is_paid = serializers.ReadOnlyField()
    patient_name = serializers.ReadOnlyField()

    class Meta:
        model = Bill
        fields = '__all__'


class BillDetailSerializer(serializers.ModelSerializer):
    record = MedicalRecordSerializer(read_only=True)
    is_paid = serializers.ReadOnlyField()
    patient_name = serializers.ReadOnlyField()

    class Meta:
        model = Bill
        fields = '__all__'
