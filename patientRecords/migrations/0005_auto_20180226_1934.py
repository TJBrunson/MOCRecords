# Generated by Django 2.0.2 on 2018-02-27 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientRecords', '0004_auto_20180226_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitinfo',
            name='follow_up_required',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AddField(
            model_name='visitinfo',
            name='visit_notes',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
