# Generated by Django 3.2.6 on 2021-08-18 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0004_gif_model_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gif_model',
            old_name='categories',
            new_name='category',
        ),
    ]