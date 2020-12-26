from django.urls import path
from project import views

app_name = 'project'

urlpatterns = [
    path('project/', views.my_projects, name='my_projects'),

]
