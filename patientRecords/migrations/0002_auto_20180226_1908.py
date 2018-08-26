# Generated by Django 2.0.2 on 2018-02-27 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientRecords', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_of_checkin', models.DateTimeField(blank=True, verbose_name='Time of Checkin')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientRecords.PatientInfo')),
            ],
        ),
        migrations.RemoveField(
            model_name='visitrecord',
            name='patient',
        ),
        migrations.DeleteModel(
            name='VisitRecord',
        ),
    ]
