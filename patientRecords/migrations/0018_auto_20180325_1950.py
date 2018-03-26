# Generated by Django 2.0.2 on 2018-03-26 01:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientRecords', '0017_auto_20180323_2246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkin',
            old_name='patient',
            new_name='patient_id',
        ),
        migrations.AlterField(
            model_name='checkout',
            name='patient',
            field=models.ForeignKey(default=datetime.datetime(2018, 3, 25, 19, 50, 22, 764008), on_delete=django.db.models.deletion.CASCADE, to='patientRecords.PatientInfo'),
        ),
    ]