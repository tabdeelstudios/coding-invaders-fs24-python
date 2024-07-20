import uuid
from django.urls import path
from .views import InvoiceView, InvoiceItemView

urlpatterns = [
    path('', InvoiceView.as_view(), name='allInvoices'),
    path('addInvoice', InvoiceView.as_view(), name='addInvoice'),
    path('editInvoice/<uuid:invoice_id>', InvoiceView.as_view(), name='updateInvoice'),
    path('deleteInvoice/<uuid:invoice_id>', InvoiceView.as_view(), name='deleteInvoice'),
    
    path('<uuid:invoice_id>/items', InvoiceItemView.as_view(), name='allItems'),
    path('<uuid:invoice_id>/items/addItem', InvoiceItemView.as_view(), name='addItem'),
    path('<uuid:invoice_id>/items/update/<uuid:itemId>', InvoiceItemView.as_view(), name='updateItem'),
    path('<uuid:invoice_id>/items/delete/<uuid:itemId>', InvoiceItemView.as_view(), name='deleteItem'),
]