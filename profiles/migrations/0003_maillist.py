# Generated by Django 4.2.9 on 2024-02-08 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]