# Generated by Django 5.0.4 on 2024-05-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewellery_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='seller_message',
            field=models.TextField(blank=True),
        ),
    ]
