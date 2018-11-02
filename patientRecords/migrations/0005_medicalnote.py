# Generated by Django 2.1 on 2018-11-02 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientRecords', '0004_auto_20181024_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_date', models.DateField(null=True)),
                ('note', models.CharField(max_length=500)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientRecords.PatientInfo')),
            ],
        ),
    ]
