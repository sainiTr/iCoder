# Generated by Django 4.1 on 2022-08-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_blogpost_btime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='btime',
            field=models.DateField(default='2022-08_08/21/22'),
        ),
    ]
