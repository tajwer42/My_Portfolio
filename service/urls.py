from django.urls import path
from service import views

app_name = 'service'

urlpatterns = [
    path('services/', views.my_service, name='my_services'),
]
