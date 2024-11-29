# resadmin/views.py  
from django.shortcuts import render, redirect  
from django.http import HttpResponse  
from rest_framework import viewsets  
from .models import Order  
from .serializers import OrderSerializer  

# Existing OrderViewSet for API  
class OrderViewSet(viewsets.ModelViewSet):  
    queryset = Order.objects.all()  
    serializer_class = OrderSerializer  

def home(request):  
    return redirect('/api/orders/')   
    