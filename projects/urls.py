from django.urls import path
from projects import views


app_name = 'projects'

urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    path('<int:pk>', views.project_detail, name='project_detail'),
]