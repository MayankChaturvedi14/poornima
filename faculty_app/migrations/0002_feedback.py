# Generated by Django 3.2.9 on 2022-02-19 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('reg_id', models.CharField(max_length=100)),
                ('review', models.TextField()),
            ],
        ),
    ]
