# Generated by Django 3.0.5 on 2020-04-20 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_info',
            new_name='Course_info',
        ),
    ]
