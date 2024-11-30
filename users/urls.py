from .views import LoginView, SignupView, google_auth
from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import (AdminViewSet, UserViewSet, MenuViewSet, FavoriteViewSet,   
                    CartViewSet, OrderViewSet, ReviewViewSet, DeliveryViewSet,   
                    LoyaltyViewSet, PaymentViewSet, DiscountViewSet)  

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('api/auth/google/', google_auth, name='google_auth'),
]



router = DefaultRouter()  
router.register(r'admins', AdminViewSet)  
router.register(r'users', UserViewSet)  
router.register(r'menu', MenuViewSet)  
router.register(r'favorites', FavoriteViewSet)  
router.register(r'carts', CartViewSet)  
router.register(r'orders', OrderViewSet)  
router.register(r'reviews', ReviewViewSet)  
router.register(r'deliveries', DeliveryViewSet)  
router.register(r'loyalty', LoyaltyViewSet)  
router.register(r'payments', PaymentViewSet)  
router.register(r'discounts', DiscountViewSet)  

urlpatterns = [  
    path('', include(router.urls)),  
]