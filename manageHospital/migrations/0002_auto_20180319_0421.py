# Generated by Django 2.0.3 on 2018-03-19 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageHospital', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors',
            name='id',
        ),
        migrations.AddField(
            model_name='doctors',
            name='doc_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
