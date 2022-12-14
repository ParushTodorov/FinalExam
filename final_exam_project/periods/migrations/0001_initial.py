# Generated by Django 4.1.3 on 2022-12-14 17:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import final_exam_project.core_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodForPreparation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(choices=[('SOUTH EASTERN', 'South Eastern'), ('SOUTH CENTRAL', 'South Central'), ('SOUTH WESTERN', 'South Western'), ('NORTH EASTERN', 'North Eastern'), ('NORTH CENTRAL', 'North Central'), ('NORTH WESTERN', 'North Western'), ('SOFIA', 'Sofia')], max_length=13, unique=True)),
                ('days_for_preparation', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='PeriodForPromo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('discount', models.FloatField(validators=[final_exam_project.core_app.validators.ValueInRangeValidator(1, 100, 'Discount must be between 1 and 100!')])),
            ],
        ),
        migrations.CreateModel(
            name='PeriodForRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('province', models.CharField(choices=[('SOUTH EASTERN', 'South Eastern'), ('SOUTH CENTRAL', 'South Central'), ('SOUTH WESTERN', 'South Western'), ('NORTH EASTERN', 'North Eastern'), ('NORTH CENTRAL', 'North Central'), ('NORTH WESTERN', 'North Western'), ('SOFIA', 'Sofia')], max_length=13)),
                ('city', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('address', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('comment', models.TextField(blank=True, max_length=100, null=True)),
                ('total_price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.cars')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
