# Generated by Django 3.2.23 on 2023-11-29 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20231125_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
