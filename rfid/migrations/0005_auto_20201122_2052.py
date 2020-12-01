# Generated by Django 3.1.3 on 2020-11-22 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rfid', '0004_auto_20201122_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='student_tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfid.student', verbose_name='Student RFID'),
        ),
    ]
