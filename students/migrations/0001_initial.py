# Generated by Django 3.0.6 on 2020-09-23 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institute', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField(blank=True, null=True)),
                ('floor', models.CharField(blank=True, choices=[('Ground', 'Ground'), ('First', 'First'), ('Second', 'Second')], max_length=10, null=True)),
                ('block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='institute.Block')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='institute.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Outing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromDate', models.DateTimeField()),
                ('toDate', models.DateTimeField()),
                ('purpose', models.CharField(max_length=150)),
                ('permission', models.CharField(choices=[('Pending', 'Pending'), ('Granted', 'Granted'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.Student')),
            ],
            options={
                'ordering': ['-fromDate'],
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present_dates', models.TextField(blank=True, null=True)),
                ('absent_dates', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='institute.Student')),
            ],
        ),
    ]
