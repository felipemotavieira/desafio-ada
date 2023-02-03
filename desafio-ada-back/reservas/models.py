from django.db import models
import uuid

# Create your models here.
class Reserva(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    referencia = models.SmallIntegerField(default=0)
    data = models.DateField()
    data_de_checkin = models.DateField()
    data_de_checkout = models.DateField()
    aluguel_com_imposto = models.CharField(max_length=40)
    aluguel_sem_imposto = models.CharField(max_length=40)
    imposto_do_aluguel = models.CharField(max_length=40)
    extras_com_imposto = models.CharField(max_length=40)
    extras_sem_imposto = models.CharField(max_length=40)
    imposto_dos_extras = models.CharField(max_length=40)
    total_da_reserva_com_imposto = models.CharField(max_length=40)
    total_da_reserva_sem_imposto = models.CharField(max_length=40)
    total_imposto = models.CharField(max_length=40)
    pagamento = models.CharField(max_length=40)
    pendente = models.CharField(max_length=40)
    nome_alojamento = models.SmallIntegerField(default=0)
    localidade = models.CharField(max_length=40)
    portal = models.CharField(max_length=40)
    comissao_calculada = models.CharField(max_length=40)
    comissao_personalizada = models.CharField(max_length=40)
