# Generated by Django 3.2.8 on 2023-06-01 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GRB', '0005_auto_20230601_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='descuentos',
            name='comision',
        ),
        migrations.RemoveField(
            model_name='descuentos',
            name='id_cuenta',
        ),
        migrations.RemoveField(
            model_name='descuentos',
            name='swap',
        ),
    ]
