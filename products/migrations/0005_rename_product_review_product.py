# Generated by Django 4.2.9 on 2024-01-30 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Product',
            new_name='product',
        ),
    ]
