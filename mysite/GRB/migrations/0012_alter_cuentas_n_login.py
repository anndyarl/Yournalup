# Generated by Django 3.2.8 on 2023-07-02 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRB', '0011_cuentas_riesgo_operacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentas',
            name='n_login',
            field=models.CharField(max_length=12, null=True, verbose_name='Login'),
        ),
    ]