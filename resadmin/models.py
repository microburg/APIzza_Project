# resadmin/models.py  
from django.db import models  

class Order(models.Model):  
    username = models.CharField(max_length=100)  
    items = models.TextField()  
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):  
        return f"Order {self.id} by {self.username}"