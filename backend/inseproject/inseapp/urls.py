from django.urls import path
from . import views

urlpatterns = [
    path('', views.getSchools),
    path('read/<str:pk>', views.getSchool)
]
