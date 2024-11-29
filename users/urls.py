from django.urls import path
from .views import LoginView, SignupView, google_auth

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('api/auth/google/', google_auth, name='google_auth'),
]