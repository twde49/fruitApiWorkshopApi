# Generated by Django 5.0.3 on 2024-10-16 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshopApi', '0006_client_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='apiKey',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
