# Generated by Django 2.0.2 on 2018-03-04 06:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientRecords', '0009_auto_20180303_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='eyecare',
            name='date_time_of_eye_exam',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 3, 23, 19, 51, 945710), verbose_name='Time of Eye Exam'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkout',
            name='patient',
            field=models.ForeignKey(default=datetime.datetime(2018, 3, 3, 23, 19, 46, 130354), on_delete=django.db.models.deletion.CASCADE, to='patientRecords.PatientInfo'),
        ),
    ]
