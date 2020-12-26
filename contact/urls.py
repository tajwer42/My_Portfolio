from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('contact/', views.my_contact, name='my_contacts'),
]
