# Generated by Django 2.1 on 2018-08-26 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientRecords', '0024_remove_checkout_date_time_of_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_complete', models.BooleanField(default=False)),
                ('visit_info_complete', models.BooleanField(default=False)),
                ('eyecare_complete', models.BooleanField(default=False)),
                ('checkout_complete', models.BooleanField(default=False)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientRecords.PatientInfo')),
            ],
        ),
    ]
