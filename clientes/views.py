from rest_framework import viewsets, filters
from .serializers import ClienteSerializer
from .models import Cliente
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
 
class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # Ordenação, Filtros e Buscas
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    # Busca não exata
    search_fields = ['nome', 'cpf']
    # Busca Exata
    filterset_fields = ['ativo']