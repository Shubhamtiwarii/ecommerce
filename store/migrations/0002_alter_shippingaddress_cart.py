# Generated by Django 5.0.2 on 2024-03-17 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='cart',
            field=models.CharField(max_length=30),
        ),
    ]
