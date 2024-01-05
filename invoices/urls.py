# urls.py
from django.urls import path, include
from .views import InvoiceListCreateView, InvoiceDetailView, InvoiceDetailListCreateView, InvoiceDetailDetailView

urlpatterns = [
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),

    path('invoices/<int:invoice_pk>/details/', InvoiceDetailListCreateView.as_view(), name='invoice-detail-list-create'),
    path('invoices/<int:invoice_pk>/details/<int:pk>/', InvoiceDetailDetailView.as_view(), name='invoice-detail-detail'),
]
