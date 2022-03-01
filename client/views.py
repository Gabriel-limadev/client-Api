from rest_framework import viewsets, filters
from .serializers import ClientsSerializer
from .models import Client
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
 
class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientsSerializer
    # Ordenação, Filtros e Buscas
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    # Busca não exata
    search_fields = ['name', 'cpf']
    # Busca Exata
    filterset_fields = ['name', 'cpf', 'active']
    # Segurança
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]