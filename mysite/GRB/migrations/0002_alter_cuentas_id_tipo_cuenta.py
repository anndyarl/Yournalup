# Generated by Django 3.2.8 on 2023-05-31 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GRB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentas',
            name='id_tipo_cuenta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GRB.tipocuenta', verbose_name='Id tipo cuenta'),
        ),
    ]