# Generated by Django 2.2.7 on 2020-07-13 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learn',
            name='learn_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 13, 21, 2, 11, 194719)),
        ),
    ]
