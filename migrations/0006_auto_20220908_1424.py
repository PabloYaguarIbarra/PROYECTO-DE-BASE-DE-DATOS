# Generated by Django 3.0.6 on 2022-09-08 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CrudBdd', '0005_proveedor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Proveedor',
            new_name='Factura',
        ),
    ]