from rest_framework import viewsets
from .serializer import ClienteSerializer
from .models import Cliente

# Create your views here.
 
class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

