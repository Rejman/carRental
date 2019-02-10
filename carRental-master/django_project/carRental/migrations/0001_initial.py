# Generated by Django 2.1.2 on 2019-02-08 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=7)),
                ('color', models.CharField(max_length=100)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('sort', models.CharField(max_length=200)),
                ('doors', models.CharField(max_length=1)),
                ('desc', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfRental', models.DateField()),
                ('dateOfReturn', models.DateField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='carRental.Car')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='carModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carRental.CarModel'),
        ),
    ]
