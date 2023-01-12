from django.urls import path
from . import views
from .views import country_info

urlpatterns = [
  
    path('country_info/<str:pk>', views.country_info , name="country_info"),
]