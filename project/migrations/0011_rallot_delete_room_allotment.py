# Generated by Django 4.1.7 on 2023-05-22 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_rename_room_allot_room_allotment'),
    ]

    operations = [
        migrations.CreateModel(
            name='rallot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomno', models.IntegerField()),
                ('teachername', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='room_allotment',
        ),
    ]
