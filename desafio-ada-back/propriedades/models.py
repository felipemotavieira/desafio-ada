from django.db import models
import uuid

# Create your models here.
class Propriedade(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    nome = models.CharField(max_length=4)
