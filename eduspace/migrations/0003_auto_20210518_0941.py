# Generated by Django 3.1.7 on 2021-05-18 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduspace', '0002_auto_20210511_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='creation_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation datetime'),
        ),
    ]
