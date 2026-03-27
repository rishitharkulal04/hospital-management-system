from django.urls import path
from .views import MedicalRecordListCreateView, MedicalRecordDetailView, RecordStatsView

urlpatterns = [
    path('', MedicalRecordListCreateView.as_view(), name='record-list-create'),
    path('stats/', RecordStatsView.as_view(), name='record-stats'),
    path('<int:pk>/', MedicalRecordDetailView.as_view(), name='record-detail'),
]
