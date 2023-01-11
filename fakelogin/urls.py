from django.urls import path
from .views import loginpage,create_user

urlpatterns = [
    path('', loginpage, name="login"),
    path('create-user/',create_user, name="create"),
]
