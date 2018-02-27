# Generated by Django 2.0.2 on 2018-02-27 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientRecords', '0003_auto_20180226_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_of_visit', models.DateTimeField(verbose_name='Time of visit')),
                ('heent', models.CharField(choices=[('Normal', 'Normal'), ('Abnormal', 'Abnormal')], max_length=8)),
                ('neck_nodes', models.CharField(choices=[('Normal', 'Normal'), ('Abnormal', 'Abnormal')], max_length=8)),
                ('chest_heart', models.CharField(choices=[('Normal', 'Normal'), ('Abnormal', 'Abnormal')], max_length=8)),
                ('abdomen', models.CharField(choices=[('Normal', 'Normal'), ('Abnormal', 'Abnormal')], max_length=8)),
                ('exterior', models.CharField(choices=[('Normal', 'Normal'), ('Abnormal', 'Abnormal')], max_length=8)),
                ('spine', models.CharField(choices=[('Normal', 'Normal'), ('Abnormal', 'Abnormal')], max_length=8)),
                ('skin', models.CharField(choices=[('Normal', 'Normal'), ('Abnormal', 'Abnormal')], max_length=8)),
                ('neuro', models.CharField(choices=[('Normal', 'Normal'), ('Abnormal', 'Abnormal')], max_length=8)),
                ('teeth', models.CharField(choices=[('Normal', 'Normal'), ('Abnormal', 'Abnormal')], max_length=8)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientRecords.PatientInfo')),
            ],
        ),
        migrations.AlterField(
            model_name='checkin',
            name='date_time_of_checkin',
            field=models.DateTimeField(verbose_name='Time of Checkin'),
        ),
    ]