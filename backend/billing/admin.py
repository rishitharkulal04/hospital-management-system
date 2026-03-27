from django.contrib import admin
from .models import Bill

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('bill_number', 'record', 'total_amount', 'date_issued', 'date_paid', 'is_paid')
    list_filter = ('date_paid',)
    search_fields = ('bill_number', 'record__name')
    readonly_fields = ('total_amount', 'date_issued')
