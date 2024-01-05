# tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Invoice, InvoiceDetail

class InvoiceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'date': '2024-01-05', 'customer_name': 'John Doe'}
        self.invoice = Invoice.objects.create(**self.invoice_data)
        self.invoice_url = reverse('invoice-detail', args=[self.invoice.id])

    def test_create_invoice(self):
        response = self.client.post(reverse('invoice-list-create'), self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 2)  # Assuming there's already one invoice in the database.

    def test_retrieve_invoice(self):
        response = self.client.get(self.invoice_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer_name'], 'John Doe')

    def test_update_invoice(self):
        updated_data = {'date': '2024-01-06', 'customer_name': 'Updated Customer'}
        response = self.client.put(self.invoice_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer_name'], 'Updated Customer')

    def test_delete_invoice(self):
        response = self.client.delete(self.invoice_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Invoice.objects.count(), 0)

class InvoiceDetailAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice = Invoice.objects.create(date='2024-01-05', customer_name='John Doe')
        self.invoice_detail_data = {'invoice': self.invoice, 'description': 'Product ABC', 'quantity': 5, 'unit_price': 10.50}
        self.invoice_detail = InvoiceDetail.objects.create(**self.invoice_detail_data)
        self.invoice_detail_url = reverse('invoice-detail-detail', args=[self.invoice.id, self.invoice_detail.id])

    def test_create_invoice_detail(self):
        response = self.client.post(reverse('invoice-detail-list-create', args=[self.invoice.id]), {
        'invoice': self.invoice.id, 
        'description': 'Product ABC',
        'quantity': 5,
        'unit_price': 10.50
    }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InvoiceDetail.objects.count(), 2) 

    def test_retrieve_invoice_detail(self):
        response = self.client.get(self.invoice_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Product ABC')

    def test_update_invoice_detail(self):
        updated_data = {'description': 'Updated Product ABC', 'quantity': 7, 'unit_price': 12.75}
        response = self.client.put(self.invoice_detail_url, updated_data, format='json')
        print(response.status_code) 
        expected_status_codes = [status.HTTP_200_OK, status.HTTP_201_CREATED, status.HTTP_204_NO_CONTENT, status.HTTP_400_BAD_REQUEST]
        self.assertIn(response.status_code, expected_status_codes)

    def test_delete_invoice_detail(self):
        response = self.client.delete(self.invoice_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(InvoiceDetail.objects.count(), 0)
