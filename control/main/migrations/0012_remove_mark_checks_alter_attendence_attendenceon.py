# Generated by Django 5.0.3 on 2024-05-21 05:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_attendence_days_remove_attendence_doubleot_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='checks',
        ),
        migrations.AlterField(
            model_name='attendence',
            name='AttendenceOn',
            field=models.DateField(default=datetime.datetime(2024, 5, 21, 8, 20, 45, 761838)),
        ),
    ]