# Generated by Django 3.2.8 on 2023-06-01 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GRB', '0003_descuentos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuentas',
            name='comision',
        ),
        migrations.RemoveField(
            model_name='cuentas',
            name='swap',
        ),
        migrations.AlterField(
            model_name='cuentas',
            name='id_tipo_cuenta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GRB.tipocuenta', verbose_name='Id tipo cuenta'),
        ),
    ]
