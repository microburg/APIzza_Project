from django.db import models  

class Admin(models.Model):  
    name = models.CharField(max_length=100)  
    password = models.CharField(max_length=100)  
    phone = models.IntegerField()  
    email = models.EmailField()  

class User(models.Model):  
    name = models.CharField(max_length=100)  
    password = models.CharField(max_length=100)  
    phone = models.IntegerField()  
    address = models.TextField()  

class Menu(models.Model):  
    category = models.CharField(max_length=100)  

class Favorite(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    items = models.ManyToManyField(Menu)  

class Cart(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    items = models.ManyToManyField(Menu)  
    totalPrice = models.FloatField()  

class Order(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    items = models.ManyToManyField(Menu)  
    totalPrice = models.FloatField()  
    orderStatus = models.CharField(max_length=50)  

class Review(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)  
    rating = models.IntegerField()  
    comment = models.TextField()  

class Delivery(models.Model):  
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  
    deliveryStatus = models.CharField(max_length=50)  
    deliveryDate = models.DateField()  
    deliveryAddress = models.TextField()  

class Loyalty(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    points = models.IntegerField()  

class Payment(models.Model):  
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  
    amount = models.FloatField()  
    paymentMethod = models.CharField(max_length=50)  
    paymentStatus = models.CharField(max_length=50)  

class Discount(models.Model):  
    discountCode = models.CharField(max_length=50)  
    description = models.TextField()  
    percentage = models.FloatField()  
    expirationDate = models.DateField()