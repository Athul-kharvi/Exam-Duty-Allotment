# Generated by Django 4.1.7 on 2023-06-12 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0034_room_allotment_room_exam_date_time_table_exam_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time_table',
            name='exam_type',
            field=models.CharField(max_length=20),
        ),
    ]