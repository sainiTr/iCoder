# Generated by Django 4.1 on 2022-08-16 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_orderaddress_cartjson'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderAddress',
            new_name='orders',
        ),
    ]
