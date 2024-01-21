from django.contrib import admin
from django.urls import path, include
from inseapp import views
from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()
router.register('schools', views.InseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schools/<int:pk>/', views.InseViewSet.as_view({'get': 'getSchoolDetail'}), name='school-detail'),
    path('schools/by-state/<int:co_uf>/', views.InseViewSet.as_view({'get': 'getSchoolByState'}),
         name='school-by-state-list'),
    path('schools/by-city/<int:co_municipio>/', views.InseViewSet.as_view({'get': 'getSchoolByCity'}),
         name='school-by-city-list'),
    path('schools/by-network-type/<int:tp_tipo_rede>/', views.InseViewSet.as_view({'get': 'getSchoolByNetworkType'}),
         name='school-by-network-type-list'),
    path('schools/by-location/<int:tp_localizacao>/', views.InseViewSet.as_view({'get': 'getSchoolByLocation'}),
         name='school-by-location-list'),
    path('schools/filtered/', views.InseViewSet.as_view({'get': 'getFilteredSchools'}),
         name='filtered-schools-list'),
    path('schools/ordered/media-inse/descending/', views.InseViewSet.as_view({'get': 'getSchoolsOrderedByDescending'}),
         name='schools-ordered-media-inse-descending'),
    path('schools/ordered/media-inse/ascending/', views.InseViewSet.as_view({'get': 'getSchoolsOrderedByAscending'}),
         name='schools-ordered-media-inse-ascending'),
    path('schools/ordered/students/descending/', views.InseViewSet.as_view({'get': 'getSchoolsOrderedByStudentsDescending'}),
         name='schools-ordered-students-descending'),
    path('schools/ordered/students/ascending/', views.InseViewSet.as_view({'get': 'getSchoolsOrderedByStudentsAscending'}),
         name='schools-ordered-students-ascending'),
    path('', include(router.urls))
]
