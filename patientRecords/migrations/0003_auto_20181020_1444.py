# Generated by Django 2.1 on 2018-10-20 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientRecords', '0002_auto_20181005_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eyecare',
            name='near',
        ),
        migrations.RemoveField(
            model_name='eyecare',
            name='pinhole',
        ),
        migrations.AddField(
            model_name='eyecare',
            name='near_left',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eyecare',
            name='near_right',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
