from django.db import models
import uuid

# Create your models here.
class Tipo(models.TextChoices):
    A_PAGA="A pagar"
    A_RECEBER="A receber"

class Conta(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    tipo = models.CharField(choices=Tipo.choices, max_length=40)
    vencimento = models.DateField()
    valor = models.FloatField()
    propriedade = models.ForeignKey(
        'propriedades.Propriedade',
        on_delete=models.CASCADE,
        related_name='propriedade'
    )
    reserva = models.ForeignKey(
        'reservas.Reserva',
        on_delete=models.CASCADE,
        related_name='conta'
    )
