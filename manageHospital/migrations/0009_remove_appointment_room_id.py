# Generated by Django 2.0.3 on 2018-03-19 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageHospital', '0008_auto_20180319_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='room_id',
        ),
    ]