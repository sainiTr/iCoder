# Generated by Django 4.1 on 2022-08-28 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_alter_blogpost_bdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='topblog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 18, 42, 34, 126482)),
        ),
        migrations.AddField(
            model_name='topblog',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='bdate',
            field=models.DateField(default=datetime.datetime(2022, 8, 28, 18, 42, 34, 126482)),
        ),
    ]
