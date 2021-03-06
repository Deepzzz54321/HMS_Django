# Generated by Django 3.0.6 on 2020-09-23 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_type', models.CharField(choices=[('Student', 'Student'), ('Official', 'Official'), ('Worker', 'Worker')], max_length=40)),
                ('entity_id', models.IntegerField()),
                ('type', models.CharField(choices=[('General', 'General'), ('Food Issues', 'Food Issues'), ('Electrical', 'Electrical'), ('Civil', 'Civil'), ('Room Cleaning', 'Room Cleaning'), ('Restroom Cleaning', 'Restroom Cleaning'), ('Indisciplinary', 'Indisciplinary'), ('Discrimination/ Harassment', 'Discrimination/ Harassment'), ('Damage to property', 'Damage to property')], max_length=40)),
                ('summary', models.CharField(max_length=200)),
                ('detailed', models.TextField()),
                ('status', models.CharField(choices=[('Registered', 'Registered'), ('Processing', 'Processing'), ('Resolved', 'Resolved')], default='Registered', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_type', models.CharField(choices=[('Student', 'Student'), ('Official', 'Official'), ('Worker', 'Worker')], max_length=40)),
                ('entity_id', models.IntegerField()),
                ('status', models.CharField(choices=[('Registered', 'Registered'), ('Resolved', 'Resolved')], default='Registered', max_length=20)),
                ('summary', models.CharField(max_length=200)),
                ('detailed', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
