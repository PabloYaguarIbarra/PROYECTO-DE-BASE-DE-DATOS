# Generated by Django 3.0.6 on 2022-09-08 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudBdd', '0006_auto_20220908_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('cod_proveedor', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('ruc', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.EmailField(max_length=50)),
            ],
        ),
    ]