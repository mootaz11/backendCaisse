# Generated by Django 3.1.5 on 2021-01-11 08:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restApi', '0018_auto_20210111_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 11, 9, 26, 33, 389932)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 11, 9, 26, 33, 408149)),
        ),
    ]
