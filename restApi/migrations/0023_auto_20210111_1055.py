# Generated by Django 3.1.5 on 2021-01-11 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restApi', '0022_auto_20210111_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 11, 10, 55, 30, 635719)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 11, 10, 55, 30, 635719)),
        ),
    ]
