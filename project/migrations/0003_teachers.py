# Generated by Django 4.1.7 on 2023-04-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_rooms'),
    ]

    operations = [
        migrations.CreateModel(
            name='teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('passwrd', models.CharField(max_length=50)),
            ],
        ),
    ]