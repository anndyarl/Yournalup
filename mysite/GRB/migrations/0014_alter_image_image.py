# Generated by Django 3.2.8 on 2023-07-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRB', '0013_auto_20230711_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Imagen'),
        ),
    ]