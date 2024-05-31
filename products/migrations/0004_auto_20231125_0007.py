# Generated by Django 3.2.23 on 2023-11-25 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20231124_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(max_length=300),
        ),
    ]