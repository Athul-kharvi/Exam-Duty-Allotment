# Generated by Django 4.1.7 on 2023-06-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0038_remove_rooms_id_remove_staff_id_remove_time_table_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time_table',
            name='exam_time',
        ),
        migrations.AddField(
            model_name='time_table',
            name='date_time',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
