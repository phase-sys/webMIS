# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    region = models.ForeignKey('Region', models.DO_NOTHING, blank=False, null=False)
    province = models.ForeignKey('Province', models.DO_NOTHING, blank=False, null=False)
    municipality = models.ForeignKey('Municipality', models.DO_NOTHING, blank=False, null=False)
    barangay = models.ForeignKey('Barangay', models.DO_NOTHING, blank=False, null=False)
    street = models.ForeignKey('Street', models.DO_NOTHING, blank=False, null=False)
    zip = models.ForeignKey('Zip', models.DO_NOTHING, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'address'


class BackgroundInfo(models.Model):
    background_info_id = models.AutoField(primary_key=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, blank=False, null=False)
    department = models.ForeignKey('Department', models.DO_NOTHING, blank=False, null=False)
    first_name = models.CharField(blank=False, null=False)
    middle_name = models.CharField(blank=True, null=True)
    last_name = models.CharField(blank=False, null=False)
    dob = models.DateField(blank=False, null=False)
    contact_number = models.CharField(blank=False, null=False)
    email = models.CharField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'background_info'


class Barangay(models.Model):
    barangay_id = models.AutoField(primary_key=True)
    barangay = models.CharField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'barangay'


class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    building_name = models.CharField(blank=False, null=False)
    description = models.CharField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'building'


class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    instructor = models.ForeignKey('Instructor', models.DO_NOTHING, blank=False, null=False)
    subject = models.ForeignKey('Subject', models.DO_NOTHING, blank=False, null=False)
    schedule = models.ForeignKey('Schedule', models.DO_NOTHING, blank=False, null=False)
    year = models.ForeignKey('SchoolYear', models.DO_NOTHING, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'class'


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(blank=False, null=False)
    description = models.CharField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'department'


class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    background_info = models.ForeignKey(BackgroundInfo, models.DO_NOTHING, blank=False, null=False)
    job_title = models.CharField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'instructor'


class Municipality(models.Model):
    municipality_id = models.AutoField(primary_key=True)
    municipality = models.CharField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'municipality'


class Province(models.Model):
    province_id = models.AutoField(primary_key=True)
    province = models.CharField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'province'


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region = models.CharField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'region'


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    building = models.ForeignKey(Building, models.DO_NOTHING, blank=False, null=False)
    room_name = models.CharField(blank=False, null=False)
    description = models.CharField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'room'


class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, models.DO_NOTHING, blank=False, null=False)
    schedule_day = models.CharField(blank=False, null=False)
    schedule_time = models.CharField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'schedule'


class SchoolYear(models.Model):
    year_id = models.AutoField(primary_key=True)
    start_date = models.CharField(blank=False, null=False)
    end_date = models.CharField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'school_year'


class Street(models.Model):
    street_id = models.AutoField(primary_key=True)
    street = models.CharField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'street'


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_code = models.IntegerField(unique=True, blank=False, null=False)
    background_info = models.ForeignKey(BackgroundInfo, models.DO_NOTHING, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'student'


class StudentClasses(models.Model):
    enrolled_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, models.DO_NOTHING, blank=False, null=False)
    class_field = models.ForeignKey(Class, models.DO_NOTHING, db_column='class_id', blank=False, null=False)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'student_classes'


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_code = models.CharField(blank=False, null=False)
    subject_name = models.CharField(blank=False, null=False)
    description = models.CharField(blank=False, null=False)
    units = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'subject'


class Zip(models.Model):
    zip_id = models.AutoField(primary_key=True)
    zip = models.CharField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'zip'
