# Generated by Django 4.1 on 2022-08-21 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_postblog_btime_alter_postblog_chead1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postblog',
            name='btime',
            field=models.DateField(blank=True, null=True),
        ),
    ]