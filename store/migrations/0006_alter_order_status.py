# Generated by Django 5.0.2 on 2024-03-22 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Pending'), (1, 'Shipped'), (2, 'Completed'), (3, 'Return')]),
        ),
    ]