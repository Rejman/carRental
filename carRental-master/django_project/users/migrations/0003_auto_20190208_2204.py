# Generated by Django 2.1.2 on 2019-02-08 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190208_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='code',
            field=models.CharField(max_length=6),
        ),
    ]