# Generated by Django 2.2.7 on 2020-07-09 04:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200709_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 10, 9, 40, 252383)),
        ),
    ]
