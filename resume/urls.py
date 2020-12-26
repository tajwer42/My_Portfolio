from django.urls import path
from resume import views

# https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name = 'resume'

urlpatterns = [
    path('resume/', views.my_about, name='my_abouts')
]
