# Generated by Django 3.1 on 2025-02-04 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('Pack', 'Pack'), ('Size', 'Size')], max_length=100),
        ),
    ]
