# Generated by Django 3.2.6 on 2021-08-29 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='img',
            field=models.ImageField(upload_to='property/'),
        ),
    ]