# Generated by Django 3.0.6 on 2022-09-08 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudBdd', '0003_remove_producto_id_tipocarne'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direccion', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
    ]
