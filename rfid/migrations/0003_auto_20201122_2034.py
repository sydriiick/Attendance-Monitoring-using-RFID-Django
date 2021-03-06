# Generated by Django 3.1.3 on 2020-11-22 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rfid', '0002_remove_attendance_student_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='student_tag',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='rfid.student', verbose_name='Student RFID'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='watch_tag',
            field=models.CharField(max_length=15, verbose_name='Watch RFID'),
        ),
    ]
