# Generated by Django 4.1.7 on 2023-05-29 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_alter_subject_subid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time_table',
            name='date_time',
        ),
        migrations.AddField(
            model_name='time_table',
            name='exam_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='time_table',
            name='exam_time',
            field=models.TimeField(default=None),
        ),
    ]
