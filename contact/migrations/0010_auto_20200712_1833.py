# Generated by Django 2.2.7 on 2020-07-12 13:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_auto_20200712_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 12, 18, 33, 57, 681935)),
        ),
    ]
