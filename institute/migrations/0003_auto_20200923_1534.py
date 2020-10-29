# Generated by Django 3.0.6 on 2020-09-23 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0002_auto_20200923_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='caretaker',
        ),
        migrations.AddField(
            model_name='official',
            name='block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='institute.Block'),
        ),
    ]