# Generated by Django 4.1.7 on 2023-05-29 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_room_allotment_edate_room_allotment_etime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room_allotment',
            name='edate',
        ),
        migrations.RemoveField(
            model_name='room_allotment',
            name='etime',
        ),
        migrations.AddField(
            model_name='room_allotment',
            name='examdate',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='room_allotment',
            name='examtime',
            field=models.TimeField(default=None, null=True),
        ),
    ]
