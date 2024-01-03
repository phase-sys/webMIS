# Generated by Django 5.0.1 on 2024-01-03 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BackgroundInfo',
            fields=[
                ('background_info_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField()),
                ('middle_name', models.CharField(blank=True, null=True)),
                ('last_name', models.CharField()),
                ('dob', models.DateField()),
                ('contact_number', models.CharField()),
                ('email', models.CharField()),
            ],
            options={
                'db_table': 'background_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Barangay',
            fields=[
                ('barangay_id', models.AutoField(primary_key=True, serialize=False)),
                ('barangay', models.CharField()),
            ],
            options={
                'db_table': 'barangay',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('building_id', models.AutoField(primary_key=True, serialize=False)),
                ('building_name', models.CharField()),
                ('description', models.CharField()),
            ],
            options={
                'db_table': 'building',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'class',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField()),
                ('description', models.CharField()),
            ],
            options={
                'db_table': 'department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('instructor_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_title', models.CharField()),
            ],
            options={
                'db_table': 'instructor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('municipality_id', models.AutoField(primary_key=True, serialize=False)),
                ('municipality', models.CharField()),
            ],
            options={
                'db_table': 'municipality',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('province_id', models.AutoField(primary_key=True, serialize=False)),
                ('province', models.CharField()),
            ],
            options={
                'db_table': 'province',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.AutoField(primary_key=True, serialize=False)),
                ('region', models.CharField()),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_name', models.CharField()),
                ('description', models.CharField()),
            ],
            options={
                'db_table': 'room',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('schedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('schedule_day', models.CharField()),
                ('schedule_time', models.CharField()),
            ],
            options={
                'db_table': 'schedule',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('year_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.CharField()),
                ('end_date', models.CharField()),
            ],
            options={
                'db_table': 'school_year',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('street_id', models.AutoField(primary_key=True, serialize=False)),
                ('street', models.CharField()),
            ],
            options={
                'db_table': 'street',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_code', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentClasses',
            fields=[
                ('enrolled_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'student_classes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_code', models.CharField()),
                ('subject_name', models.CharField()),
                ('description', models.CharField()),
                ('units', models.IntegerField()),
            ],
            options={
                'db_table': 'subject',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zip',
            fields=[
                ('zip_id', models.AutoField(primary_key=True, serialize=False)),
                ('zip', models.CharField()),
            ],
            options={
                'db_table': 'zip',
                'managed': False,
            },
        ),
    ]
