# Generated by Django 5.0.3 on 2024-03-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazin', '0003_rename_magazine_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
    ]
