import uuid
from django.db import models

# Invoice -> id(UUID), createdAt, updatedAt, title, status, totalAmount, clientName
class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256)
    status = models.BooleanField(default=False)
    totalAmount = models.DecimalField(decimal_places=2, max_digits=10)
    clientName = models.CharField(max_length=256)

    class Meta:
        db_table = 'invoices'
        ordering = ['-updatedAt']

        def __str__(self) -> str:
            return self.title
        

# InvoiceItem -> id, createdAt, updatedAt, rate, quantity, description
class InvoiceItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    rate = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()
    invoiceID = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)

    class Meta:
        db_table = 'items'
        ordering = ['-updatedAt']

        def __str__(self) -> str:
            return self.description
