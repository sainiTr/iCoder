# Generated by Django 4.1 on 2022-08-21 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_blogpost_about_alter_blogpost_bdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='about',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='bdate',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 0, 57, 5, 308934)),
        ),
    ]
