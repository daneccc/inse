from django.contrib import admin
from django.urls import path, include
from inseapp.views import inse_view
from rest_framework import routers
from django.urls import include
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView

router = routers.DefaultRouter()
router.register('schools', inse_view.InseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schools/<int:pk>/', inse_view.InseViewSet.as_view({'get': 'getSchoolDetail'}), name='school-detail'),
    path('schools/by-state/<int:co_uf>/', inse_view.InseViewSet.as_view({'get': 'getSchoolByState'}),
         name='school-by-state-list'),
    path('schools/by-city/<int:co_municipio>/', inse_view.InseViewSet.as_view({'get': 'getSchoolByCity'}),
         name='school-by-city-list'),
    path('schools/by-network-type/<int:tp_tipo_rede>/', inse_view.InseViewSet.as_view({'get': 'getSchoolByNetworkType'}),
         name='school-by-network-type-list'),
    path('schools/by-location/<int:tp_localizacao>/', inse_view.InseViewSet.as_view({'get': 'getSchoolByLocation'}),
         name='school-by-location-list'),
    path('schools/filtered/', inse_view.InseViewSet.as_view({'get': 'getFilteredSchools'}),
         name='filtered-schools-list'),
    path('schools/ordered/media-inse/descending/', inse_view.InseViewSet.as_view({'get': 'getSchoolsOrderedByDescending'}),
         name='schools-ordered-media-inse-descending'),
    path('schools/ordered/media-inse/ascending/', inse_view.InseViewSet.as_view({'get': 'getSchoolsOrderedByAscending'}),
         name='schools-ordered-media-inse-ascending'),
    path('schools/ordered/students/descending/', inse_view.InseViewSet.as_view({'get': 'getSchoolsOrderedByStudentsDescending'}),
         name='schools-ordered-students-descending'),
    path('schools/ordered/students/ascending/', inse_view.InseViewSet.as_view({'get': 'getSchoolsOrderedByStudentsAscending'}),
         name='schools-ordered-students-ascending'),
    path('schools/unique-ufs/', inse_view.InseViewSet.as_view({'get': 'getUniqueUfs'}),
         name='unique-ufs-list'),
    path('', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]
