from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Conta
from .serializers import ContaSerializer
from .utils import criar_objs_contas


# Create your views here.
class ContaFilter(filters.FilterSet):
    tipo = filters.CharFilter(
        field_name='tipo', lookup_expr='icontains'
    )
    vencimento = filters.CharFilter(
        field_name='vencimento', lookup_expr='icontains'
    )
    propriedade = filters.CharFilter(
        field_name='propriedade', lookup_expr='exact'
    )

    class Meta:
        model = Conta
        fields = ['tipo']

class ContaView(generics.ListCreateAPIView):
    serializer_class = ContaSerializer
    queryset = Conta.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ContaFilter
    
    def post(self, request):
        
        for index, reserva in enumerate(request.data):
            dicts_contas: tuple = criar_objs_contas(reserva)
            print('-' * 150)
            print(reserva)
            print(dicts_contas)
            for conta in dicts_contas:
                serializer = ContaSerializer(data=conta, context={'request': request, 'index': index})
                serializer.is_valid(raise_exception=True)
                serializer.save()

        contas_registradas = Conta.objects.all().values()

        return Response(contas_registradas, status.HTTP_201_CREATED)
