# Generated by Django 5.0.3 on 2024-03-13 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazin', '0004_shop_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='time_create',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='time_update',
        ),
    ]
