from rest_framework import serializers
from .models import MedicalRecord

class MedicalRecordSerializer(serializers.ModelSerializer):
    condition_display = serializers.CharField(source='get_condition_display', read_only=True)

    class Meta:
        model = MedicalRecord
        fields = '__all__'
