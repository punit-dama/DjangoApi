# Generated by Django 4.1.5 on 2023-01-26 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='order_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payment_details',
            name='order_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='status',
            name='order_id',
            field=models.IntegerField(),
        ),
    ]
