# Generated by Django 3.1.3 on 2020-11-22 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfid', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='student_tag',
        ),
    ]