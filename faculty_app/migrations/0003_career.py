# Generated by Django 3.2.9 on 2022-02-19 09:13

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_app', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('birth_place', models.CharField(max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('applied_for', models.CharField(max_length=50)),
                ('designation', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=50)),
                ('UG', models.CharField(max_length=10)),
                ('PG', models.CharField(max_length=10)),
                ('DOC', models.CharField(max_length=10)),
                ('Teaching_since', models.CharField(max_length=10)),
                ('Corporate_experience', models.CharField(max_length=10)),
                ('percentage', models.IntegerField()),
                ('areaofexp', models.CharField(max_length=50)),
                ('thesis_title', models.CharField(max_length=50)),
                ('passing_year', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
                ('college', models.CharField(max_length=50)),
                ('university', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=10)),
                ('resume', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
    ]