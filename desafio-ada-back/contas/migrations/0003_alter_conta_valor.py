# Generated by Django 4.1.6 on 2023-02-01 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_conta_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='valor',
            field=models.FloatField(),
        ),
    ]
