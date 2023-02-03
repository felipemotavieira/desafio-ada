from django.shortcuts import render
from rest_framework import generics
from .models import Propriedade
from .serializer import PropriedadeSerializer
from django_filters import rest_framework as filters

# Create your views here.
class PropriedadeFilter(filters.FilterSet):
    nome = filters.CharFilter(
        field_name='nome', lookup_expr='exact'
    )

    class Meta:
        model = Propriedade
        fields = ['nome']

class PropriedadeView(generics.ListCreateAPIView):
    serializer_class = PropriedadeSerializer
    queryset = Propriedade.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PropriedadeFilter
