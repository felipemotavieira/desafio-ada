# Generated by Django 4.1.6 on 2023-02-01 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_alter_reserva_localidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='aluguel_com_imposto',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='aluguel_sem_imposto',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='comissao_calculada',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='comissao_personalizada',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='extras_com_imposto',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='extras_sem_imposto',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='imposto_do_aluguel',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='imposto_dos_extras',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='nome_alojamento',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='pagamento',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='pendente',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='referencia',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='total_da_reserva_com_imposto',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='total_da_reserva_sem_imposto',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='total_imposto',
            field=models.FloatField(default=0.0),
        ),
    ]
