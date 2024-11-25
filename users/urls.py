from django.urls import path  
from .views import user_list

app_name = "users"  

urlpatterns = [  
    path("", user_list, name="users")
]  