from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from client.views import ClientsViewSet

routers = routers.DefaultRouter()
routers.register('clients', ClientsViewSet, basename='clients')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routers.urls))
]
