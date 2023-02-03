from .models import Reserva

class ReseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
