# Generated by Django 5.1.7 on 2025-03-10 14:26

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cereal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('shelf', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)])),
                ('weight', models.FloatField()),
                ('cups', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(choices=[('A', 'American Home Food Products'), ('G', 'General Mills'), ('K', 'Kelloggs'), ('N', 'Nabisco'), ('P', 'Post'), ('Q', 'Quaker Oats'), ('R', 'Ralston Purina')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ThermalType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(choices=[('C', 'Cold'), ('H', 'Hot')], default='C', max_length=1, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('cereal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cereal_api.cereal')),
                ('calories', models.PositiveIntegerField()),
                ('protein', models.PositiveIntegerField()),
                ('fat', models.PositiveIntegerField()),
                ('sodium', models.PositiveIntegerField()),
                ('fiber', models.FloatField()),
                ('carbo', models.FloatField()),
                ('sugars', models.PositiveIntegerField()),
                ('potass', models.PositiveIntegerField()),
                ('vitamins', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='cereal',
            name='mfd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cereal_api.manufacturer'),
        ),
        migrations.AddField(
            model_name='cereal',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cereal_api.thermaltype'),
        ),
    ]
