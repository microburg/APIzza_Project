from rest_framework import serializers  
from .models import Admin, User, Menu, Favorite, Cart, Order, Review, Delivery, Loyalty, Payment, Discount  

class AdminSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Admin  
        fields = '__all__'  

class UserSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = '__all__'  

class MenuSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Menu  
        fields = '__all__'  

class FavoriteSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Favorite  
        fields = '__all__'  

class CartSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Cart  
        fields = '__all__'  

class OrderSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Order  
        fields = '__all__'  

class ReviewSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Review  
        fields = '__all__'  

class DeliverySerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Delivery  
        fields = '__all__'  

class LoyaltySerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Loyalty  
        fields = '__all__'  

class PaymentSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Payment  
        fields = '__all__'  

class DiscountSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Discount  
        fields = '__all__'