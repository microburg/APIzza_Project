# payment/serializers.py
from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'amount', 'card_number', 'expiry_date', 'cvv', 'is_successful', 'transaction_date']
# apizza_backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('payment.urls')),  # إضافة API الدفع
]
