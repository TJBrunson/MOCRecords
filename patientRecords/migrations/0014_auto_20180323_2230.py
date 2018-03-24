# Generated by Django 2.0.2 on 2018-03-24 04:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientRecords', '0013_auto_20180314_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='bmi',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='diastolic',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='heart_rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='systolic',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='weight',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='patient',
            field=models.ForeignKey(default=datetime.datetime(2018, 3, 23, 22, 30, 0, 118833), on_delete=django.db.models.deletion.CASCADE, to='patientRecords.PatientInfo'),
        ),
    ]
