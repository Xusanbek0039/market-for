# Generated by Django 3.2.23 on 2023-11-22 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_size',
        ),
    ]