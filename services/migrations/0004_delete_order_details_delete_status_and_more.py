# Generated by Django 4.1.5 on 2023-01-26 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_remove_order_details_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order_details',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AddField(
            model_name='payment_details',
            name='status',
            field=models.BooleanField(default=0),
        ),
    ]
