from django.db import models

# Create your models here.
# payment/models.py
from django.db import models

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)  # مثلاً MM/YY
    cvv = models.CharField(max_length=3)
    is_successful = models.BooleanField(default=False)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} - {'Success' if self.is_successful else 'Failed'}"

