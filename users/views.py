import json
import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import id_token
from rest_framework.decorators import api_view
from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets  
from .models import Admin, User, Menu, Favorite, Cart, Order, Review, Delivery, Loyalty, Payment, Discount  
from .serializers import (AdminSerializer, UserSerializer, MenuSerializer, FavoriteSerializer,   
                          CartSerializer, OrderSerializer, ReviewSerializer, DeliverySerializer,   
                          LoyaltySerializer, PaymentSerializer, DiscountSerializer)  

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({"error": "Invalid credentials"}, status=401)


class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=400)
        
        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already registered"}, status=400)

        # Create the user and save it
        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password)  # Hash the password before storing
        )

        return Response({"message": "User created successfully!"}, status=201)


import logging

@api_view(['POST'])
def google_auth(request):
    try:
        token = request.data.get('token')
        if not token:
            return Response({'success': False, 'error': 'Token not provided'}, status=400)
        
        # Verify token
        id_info = id_token.verify_oauth2_token(token, Request(), settings.GOOGLE_CLIENT_ID)
        logging.info(f"ID Token Info: {id_info}")
        
        email = id_info.get('email')
        username = id_info.get('name')
        logging.info(f"Google User Info: Email - {email}, Username - {username}")

        # Create or get user
        user, created = User.objects.get_or_create(username=username, email=email)

        if created:
            user.set_unusable_password()
            user.save()

        return Response({'success': True, 'username': user.username})

    except ValueError as e:
        logging.error(f"Token verification failed: {e}")
        return Response({'success': False, 'error': 'Invalid token'}, status=400)

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return Response({'success': False, 'error': 'Something went wrong'}, status=500)



class AdminViewSet(viewsets.ModelViewSet):  
    queryset = Admin.objects.all()  
    serializer_class = AdminSerializer  

class UserViewSet(viewsets.ModelViewSet):  
    queryset = User.objects.all()  
    serializer_class = UserSerializer  

class MenuViewSet(viewsets.ModelViewSet):  
    queryset = Menu.objects.all()  
    serializer_class = MenuSerializer  

class FavoriteViewSet(viewsets.ModelViewSet):  
    queryset = Favorite.objects.all()  
    serializer_class = FavoriteSerializer  

class CartViewSet(viewsets.ModelViewSet):  
    queryset = Cart.objects.all()  
    serializer_class = CartSerializer  

class OrderViewSet(viewsets.ModelViewSet):  
    queryset = Order.objects.all()  
    serializer_class = OrderSerializer  

class ReviewViewSet(viewsets.ModelViewSet):  
    queryset = Review.objects.all()  
    serializer_class = ReviewSerializer  

class DeliveryViewSet(viewsets.ModelViewSet):  
    queryset = Delivery.objects.all()  
    serializer_class = DeliverySerializer  

class LoyaltyViewSet(viewsets.ModelViewSet):  
    queryset = Loyalty.objects.all()  
    serializer_class = LoyaltySerializer  

class PaymentViewSet(viewsets.ModelViewSet):  
    queryset = Payment.objects.all()  
    serializer_class = PaymentSerializer  

class DiscountViewSet(viewsets.ModelViewSet):  
    queryset = Discount.objects.all()  
    serializer_class = DiscountSerializer