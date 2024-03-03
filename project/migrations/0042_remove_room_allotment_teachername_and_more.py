# Generated by Django 4.1.7 on 2023-07-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0041_rename_sid_room_allotment_tid_remove_rooms_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room_allotment',
            name='teachername',
        ),
        migrations.AddField(
            model_name='room_allotment',
            name='staff_id',
            field=models.CharField(default=-2011, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room_allotment',
            name='tid',
            field=models.CharField(default=None, max_length=12),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='dept',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='roomloc',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.EmailField(max_length=12),
        ),
        migrations.AlterField(
            model_name='staff',
            name='passwrd',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='staff',
            name='username',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='subject',
            name='stream',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subcode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='time_table',
            name='sid',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='time_table',
            name='tid',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]