# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class CamsLogin(models.Model):
    userid = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cams_login'


class ClassTchr(models.Model):
    fid = models.ForeignKey('FacultyList', models.DO_NOTHING, db_column='fid',primary_key=True)
    section = models.CharField(max_length=1)
    sem = models.BooleanField(primary_key=True)
    year = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'class_tchr'
        unique_together = (('fid', 'sem', 'year'),)


class FacultyEnr(models.Model):
    eno = models.FloatField(primary_key=True)
    fid = models.ForeignKey('FacultyList', models.DO_NOTHING, db_column='fid')
    slot = models.BooleanField()
    day = models.CharField(max_length=3)
    section = models.CharField(max_length=1)
    year = models.IntegerField()
    sem = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'faculty_enr'


class FacultyList(models.Model):
    fid = models.ForeignKey(CamsLogin, models.DO_NOTHING, db_column='fid', primary_key=True)
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    branch = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faculty_list'


class FacultyResponsibility(models.Model):
    fid = models.ForeignKey(FacultyList, models.DO_NOTHING, db_column='fid')
    responsibility = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'faculty_responsibility'
        unique_together = (('fid', 'responsibility'),)


class StudentAtt(models.Model):
    usn = models.ForeignKey('StudentList', models.DO_NOTHING, db_column='usn')
    eno = models.ForeignKey(FacultyEnr, models.DO_NOTHING, db_column='eno')
    dte = models.DateField()

    class Meta:
        managed = False
        db_table = 'student_att'
        unique_together = (('usn', 'eno', 'dte'),)


class StudentClassenr(models.Model):
    usn = models.ForeignKey('StudentList', models.DO_NOTHING, db_column='usn')
    eno = models.ForeignKey(FacultyEnr, models.DO_NOTHING, db_column='eno')

    class Meta:
        managed = False
        db_table = 'student_classenr'
        unique_together = (('usn', 'eno'),)


class StudentList(models.Model):
    usn = models.ForeignKey(CamsLogin, models.DO_NOTHING, db_column='usn', primary_key=True)
    name = models.CharField(max_length=30)
    joining = models.DateField()
    address = models.CharField(max_length=300, blank=True, null=True)
    phno = models.CharField(max_length=15)
    parent_phno = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'student_list'


class StudentSemenr(models.Model):
    usn = models.ForeignKey(StudentList, models.DO_NOTHING, db_column='usn')
    branch = models.CharField(max_length=2)
    sem = models.BooleanField()
    section = models.CharField(max_length=1)
    mentorid = models.ForeignKey(FacultyList, models.DO_NOTHING, db_column='mentorid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_semenr'
        unique_together = (('usn', 'sem', 'section'),)


class SubjectList(models.Model):
    scode = models.CharField(max_length=8)
    sname = models.CharField(max_length=100)
    branch = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'subject_list'
        unique_together = (('scode', 'branch'),)


class TestId(models.Model):
    tid = models.CharField(primary_key=True, max_length=9)
    year = models.IntegerField()
    slot = models.CharField(max_length=1)
    branch = models.CharField(max_length=2)
    sem = models.CharField(max_length=1, blank=True, null=True)
    tno = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'test_id'


class TestNo(models.Model):
    tid = models.ForeignKey(TestId, models.DO_NOTHING, db_column='tid', primary_key=True)
    scode = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'test_no'


class WriteTest(models.Model):
    usn = models.ForeignKey(StudentList, models.DO_NOTHING, db_column='usn')
    tid = models.ForeignKey(TestNo, models.DO_NOTHING, db_column='tid')
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'write_test'
        unique_together = (('usn', 'tid'),)
