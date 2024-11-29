from django.contrib import admin  
from django.urls import path, include  
from resadmin.views import home  # Import the new home view  

urlpatterns = [  
    path('', home, name='home'),  # Add the home view for the root URL  
    path('admin/', admin.site.urls),  
    path('api/', include('resadmin.urls')),  # Include the resadmin API URLs  
    path('api/', include('users.urls')),  # Include the users API URLs
]