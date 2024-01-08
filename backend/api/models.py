from django.db import models


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=255, default=None, blank=False, null=False)
    description = models.CharField(max_length=255, default=None, blank=False, null=False)


class Barangay(models.Model):
    barangay_id = models.AutoField(primary_key=True)
    barangay = models.CharField(max_length=255, default=None, blank=False, null=False)


class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    building_name = models.CharField(max_length=255, default=None, blank=False, null=False)
    description = models.CharField(max_length=255, default=None, blank=False, null=False)


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_code = models.CharField(max_length=255, default=None, blank=False, null=False)
    subject_name = models.CharField(max_length=255, default=None, blank=False, null=False)
    description = models.CharField(max_length=255, default=None, blank=False, null=False)
    units = models.IntegerField(blank=False, null=False)


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, blank=False, null=False)
    room_name = models.CharField(max_length=255, default=None, blank=False, null=False)
    description = models.CharField(max_length=255, default=None, blank=False, null=False)


class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=False, null=False)
    schedule_day = models.CharField(max_length=255, default=None, blank=False, null=False)
    schedule_time = models.CharField(max_length=255, default=None, blank=False, null=False)


class SchoolYear(models.Model):
    year_id = models.AutoField(primary_key=True)
    start_date = models.CharField(max_length=255, default=None, blank=False, null=False)
    end_date = models.CharField(max_length=255, default=None, blank=False, null=False)


class Municipality(models.Model):
    municipality_id = models.AutoField(primary_key=True)
    municipality = models.CharField(max_length=255, default=None, blank=False, null=False)


class Province(models.Model):
    province_id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=255, default=None, blank=False, null=False)


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region = models.CharField(max_length=255, default=None, blank=False, null=False)


class Street(models.Model):
    street_id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=255, default=None, blank=False, null=False)


class Zip(models.Model):
    zip_id = models.AutoField(primary_key=True)
    zip = models.CharField(max_length=255, default=None, blank=False, null=False)


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=False, null=False)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, blank=False, null=False)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, blank=False, null=False)
    barangay = models.ForeignKey(Barangay, on_delete=models.CASCADE, blank=False, null=False)
    street = models.ForeignKey(Street, on_delete=models.CASCADE, blank=False, null=False)
    zip = models.ForeignKey(Zip, on_delete=models.CASCADE, blank=False, null=False)


class BackgroundInfo(models.Model):
    background_info_id = models.AutoField(primary_key=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=False, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=False, null=False)
    first_name = models.CharField(max_length=255, default=None, blank=False, null=False)
    middle_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=255, default=None, blank=False, null=False)
    dob = models.DateField(blank=False, null=False)
    contact_number = models.CharField(max_length=255, default=None, blank=False, null=False)
    email = models.CharField(max_length=255, default=None, blank=False, null=False)


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_code = models.IntegerField(unique=True, blank=False, null=False)
    background_info = models.ForeignKey(BackgroundInfo, on_delete=models.CASCADE, blank=False, null=False)


class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    background_info = models.ForeignKey(BackgroundInfo, on_delete=models.CASCADE, blank=False, null=False)
    job_title = models.CharField(max_length=255, default=None, blank=False, null=False)


class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=False, null=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=False, null=False)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, blank=False, null=False)
    year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE, blank=False, null=False)


class StudentClasses(models.Model):
    enrolled_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False, null=False)
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_id', blank=False, null=False)
