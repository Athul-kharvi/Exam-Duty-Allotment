# Generated by Django 4.1.7 on 2023-04-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_delete_seatallotment'),
    ]

    operations = [
        migrations.CreateModel(
            name='autoseatadd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomno', models.CharField(max_length=100)),
                ('teachername', models.CharField(max_length=100)),
            ],
        ),
    ]
