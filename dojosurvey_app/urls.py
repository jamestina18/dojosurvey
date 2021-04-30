from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey),
    path('add-user', views.add_user)
]