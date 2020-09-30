from django.urls import path
from admins import login
urlpatterns = [
    path('signin', login.signin)
]