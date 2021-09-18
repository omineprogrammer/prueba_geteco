from django.urls import path
from .views import *


app_name = 'solicitud'
urlpatterns = [
    path('', RegistroListView.as_view(), name='index'),
    
    # Registro
    path('registro/', RegistroListView.as_view(), 
         name='registro-list'),
    path('registro/add/', RegistroCreateView.as_view(),
         name='registro-add'),
    path('registro/<int:pk>/', RegistroUpdateView.as_view(), 
         name='registro-update'),
    path('registro/<int:pk>/delete/', RegistroDeleteView.as_view(), 
         name='registro-delete'),

    # Ciudad
    path('ciudad/', CiudadListView.as_view(),
         name='ciudad-list'),
    path('ciudad/add/', CiudadCreateView.as_view(),
         name='ciudad-add'),
    path('ciudad/<int:pk>/', CiudadUpdateView.as_view(),
         name='ciudad-update'),
    path('ciudad/<int:pk>/delete/', CiudadDeleteView.as_view(),
         name='ciudad-delete'),

    # Empresa
    path('empresa/', EmpresaListView.as_view(),
         name='empresa-list'),
    path('empresa/add/', EmpresaCreateView.as_view(),
         name='empresa-add'),
    path('empresa/<int:pk>/', EmpresaUpdateView.as_view(),
         name='empresa-update'),
    path('empresa/<int:pk>/delete/', EmpresaDeleteView.as_view(),
         name='empresa-delete'),

]
