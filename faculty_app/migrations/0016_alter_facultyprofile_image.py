# Generated by Django 3.2.9 on 2022-04-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_app', '0015_alter_facultyprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultyprofile',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='profile_image'),
        ),
    ]