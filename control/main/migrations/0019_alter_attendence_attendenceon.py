# Generated by Django 5.0.6 on 2024-05-27 17:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_attendence_attendenceon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='AttendenceOn',
            field=models.DateField(default=datetime.datetime(2024, 5, 27, 20, 49, 31, 142478)),
        ),
    ]
