from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clientes.views import ClientesViewSet

routers = routers.DefaultRouter()
routers.register('clientes', ClientesViewSet, basename='Clientes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routers.urls))
]
