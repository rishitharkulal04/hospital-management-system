from django.urls import path
from .views import BillListCreateView, BillDetailView, MarkBillPaidView, BillingStatsView

urlpatterns = [
    path('', BillListCreateView.as_view(), name='bill-list-create'),
    path('stats/', BillingStatsView.as_view(), name='billing-stats'),
    path('<int:pk>/', BillDetailView.as_view(), name='bill-detail'),
    path('<int:pk>/mark-paid/', MarkBillPaidView.as_view(), name='bill-mark-paid'),
]
