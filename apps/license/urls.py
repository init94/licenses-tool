from django.urls import path

from apps.license.views import index, license_view, license_list, license_edit, license_delete, LicenseAPI

app_name = "license"

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', license_view, name='license_create'),
    path('listar', license_list, name='license_list'),
    path('editar/<int:id_license>/', license_edit, name='license_edit'),
    path('eliminar/<int:id_license>/', license_delete, name='license_delete'),
    path('api', LicenseAPI.as_view(), name='api'),
]