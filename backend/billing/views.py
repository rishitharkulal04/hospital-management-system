from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .models import Bill
from .serializers import BillSerializer, BillDetailSerializer


class BillListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/billing/        — list all bills (?paid=true/false to filter)
    POST /api/billing/        — create new bill (send record ID, not patient name)
    """
    queryset = Bill.objects.all().order_by('-date_issued')
    serializer_class = BillSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        paid = self.request.query_params.get('paid')
        if paid == 'true':
            qs = qs.filter(date_paid__isnull=False)
        elif paid == 'false':
            qs = qs.filter(date_paid__isnull=True)
        return qs


class BillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillDetailSerializer


class MarkBillPaidView(APIView):
    """POST /api/billing/<id>/mark-paid/"""
    def post(self, request, pk):
        try:
            bill = Bill.objects.get(pk=pk)
        except Bill.DoesNotExist:
            return Response({'error': 'Bill not found'}, status=status.HTTP_404_NOT_FOUND)

        if bill.date_paid:
            return Response({'message': 'Bill already paid', 'bill': BillSerializer(bill).data})

        bill.date_paid = timezone.now().date()
        bill.save()
        return Response({
            'message': 'Bill marked as paid',
            'bill': BillSerializer(bill).data
        })


class BillingStatsView(APIView):
    """GET /api/billing/stats/"""
    def get(self, request):
        from django.db.models import Sum
        all_bills = Bill.objects.all()
        paid_bills = all_bills.filter(date_paid__isnull=False)
        pending_bills = all_bills.filter(date_paid__isnull=True)

        total_billed = all_bills.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
        total_collected = paid_bills.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
        total_pending = pending_bills.aggregate(Sum('total_amount'))['total_amount__sum'] or 0

        return Response({
            'total_bills': all_bills.count(),
            'paid_bills': paid_bills.count(),
            'pending_bills': pending_bills.count(),
            'total_billed': float(total_billed),
            'total_collected': float(total_collected),
            'total_pending': float(total_pending),
        })
