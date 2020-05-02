# Generated by Django 3.0.5 on 2020-04-30 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_attendance_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outing',
            name='permission',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Granted', 'Granted'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
        ),
    ]
