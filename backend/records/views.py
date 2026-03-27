from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer


class MedicalRecordListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/records/        — list all records (supports ?search=name&condition=FLU)
    POST /api/records/        — create a new record
    """
    queryset = MedicalRecord.objects.all().order_by('-date_of_visit')
    serializer_class = MedicalRecordSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'condition', 'doctor_notes']

    def get_queryset(self):
        qs = super().get_queryset()
        condition = self.request.query_params.get('condition')
        if condition and condition != 'ALL':
            qs = qs.filter(condition=condition)
        return qs


class MedicalRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/records/<id>/  — retrieve single record
    PUT    /api/records/<id>/  — full update
    PATCH  /api/records/<id>/  — partial update
    DELETE /api/records/<id>/  — delete record
    """
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer


class RecordStatsView(APIView):
    """
    GET /api/records/stats/  — dashboard stats
    """
    def get(self, request):
        total = MedicalRecord.objects.count()
        admitted = MedicalRecord.objects.filter(date_of_exit__isnull=True).count()
        discharged = MedicalRecord.objects.filter(date_of_exit__isnull=False).count()
        condition_counts = {}
        for code, label in MedicalRecord.CONDITION_CHOICES:
            condition_counts[code] = MedicalRecord.objects.filter(condition=code).count()
        return Response({
            'total_records': total,
            'currently_admitted': admitted,
            'discharged': discharged,
            'by_condition': condition_counts,
        })
