# Generated by Django 2.2.7 on 2020-07-09 04:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20200709_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 10, 21, 17, 115723)),
        ),
    ]