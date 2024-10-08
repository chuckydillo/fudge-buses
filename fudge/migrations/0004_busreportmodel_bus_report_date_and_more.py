# Generated by Django 4.2.16 on 2024-10-01 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fudge', '0003_busreportmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='busreportmodel',
            name='bus_report_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='busreportmodel',
            name='bus_delay_time',
            field=models.CharField(blank=True, choices=[('0-5', 'Less than 5 minutes'), ('5-10', 'Between 5 and 10 minutes'), ('10-20', 'between 10 and 20 minutes'), ('20+', 'More than 20 minutes')], max_length=30),
        ),
    ]
