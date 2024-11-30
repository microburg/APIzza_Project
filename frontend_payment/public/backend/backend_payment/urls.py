# payment/urls.py
from django.urls import path
from .views import PaymentView

urlpatterns = [
    path('pay/', PaymentView.as_view(), name='payment-api'),
]

