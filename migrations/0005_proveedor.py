# Generated by Django 3.0.6 on 2022-09-08 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudBdd', '0004_direccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('numfac', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
