# Generated by Django 3.2.6 on 2021-08-18 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0002_auto_20210817_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gif_model',
            name='category',
        ),
    ]