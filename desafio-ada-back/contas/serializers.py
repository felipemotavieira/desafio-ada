from rest_framework import serializers
from .models import Conta, Tipo
from .utils import convert_to_data_type
from propriedades.models import Propriedade
from reservas.models import Reserva


class ContaSerializer(serializers.ModelSerializer):
    propriedade = serializers.SerializerMethodField()
    reserva = serializers.SerializerMethodField()

    class Meta:
        model = Conta
        fields = [
            'tipo',
            'vencimento',
            'valor',
            'propriedade',
            'reserva',
            'id'
        ]
        depth = 1

    def get_propriedade(self, obj):
        return obj.propriedade.nome

    def get_reserva(self, obj):
        return obj.reserva.referencia

    def create(self, validated_data):
        index = self.context['index']
        request_data = self.context['request'].data[index]

        propriedade = Propriedade.objects.get_or_create(nome=request_data['nome_alojamento'])
        reserva_dados_prontos = convert_to_data_type(request_data)

        reserva = Reserva.objects.get_or_create(**request_data)

        validated_data['propriedade'] = propriedade[0]
        validated_data['reserva'] = reserva[0]

        conta = Conta.objects.get_or_create(**validated_data)
        
        if conta[1] is False:
            raise Exception('Conta já registrada')

        return conta
    