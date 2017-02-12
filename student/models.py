# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Att(models.Model):
    satt = models.FloatField(primary_key=True)
    usn = models.ForeignKey('StudentList', models.DO_NOTHING, db_column='usn', blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    slot = models.FloatField(blank=True, null=True)
    scode = models.CharField(max_length=8, blank=True, null=True)
    poa = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att'


class CamsLogin(models.Model):
    userid = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cams_login'


class ClassTchr(models.Model):
    scfid = models.FloatField(primary_key=True)
    fid = models.ForeignKey('FacultyList', models.DO_NOTHING, db_column='fid', blank=True, null=True)
    section = models.CharField(max_length=1)
    sem = models.FloatField(blank=True, null=True)
    year = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_tchr'


class DeptSubEnr(models.Model):
    ssnor = models.FloatField(primary_key=True)
    scode = models.CharField(max_length=8, blank=True, null=True)
    sname = models.CharField(max_length=80, blank=True, null=True)
    branch = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dept_sub_enr'


class FacEnr(models.Model):
    sfid = models.FloatField(primary_key=True)
    fid = models.ForeignKey('FacultyList', models.DO_NOTHING, db_column='fid', blank=True, null=True)
    slot = models.FloatField(blank=True, null=True)
    day = models.CharField(max_length=3, blank=True, null=True)
    section = models.CharField(max_length=1)
    branch = models.CharField(max_length=2, blank=True, null=True)
    year = models.FloatField(blank=True, null=True)
    scode = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fac_enr'


class FacultyList(models.Model):
    fid = models.ForeignKey(CamsLogin, models.DO_NOTHING, db_column='fid', primary_key=True)
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    branch = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faculty_list'


class StudentList(models.Model):
    usn = models.ForeignKey(CamsLogin, models.DO_NOTHING, db_column='usn', primary_key=True)
    sname = models.CharField(max_length=30, blank=True, null=True)
    year_of_joining = models.CharField(max_length=4, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    parent_phno = models.FloatField(blank=True, null=True)
    phno = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_list'


class StudentSemEnr(models.Model):
    senr = models.FloatField(primary_key=True)
    usn = models.ForeignKey(StudentList, models.DO_NOTHING, db_column='usn', blank=True, null=True)
    branch = models.CharField(max_length=2, blank=True, null=True)
    sem = models.FloatField(blank=True, null=True)
    batch = models.FloatField(blank=True, null=True)
    section = models.CharField(max_length=1, blank=True, null=True)
    year = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_sem_enr'


class TestSub(models.Model):
    sts = models.FloatField(primary_key=True)
    ttno = models.ForeignKey('TestTme', models.DO_NOTHING, db_column='ttno', blank=True, null=True)
    scode = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_sub'


class TestTme(models.Model):
    stno = models.FloatField(primary_key=True)
    tno = models.FloatField(blank=True, null=True)
    dte = models.DateField(blank=True, null=True)
    slot = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_tme'


class WriteTest(models.Model):
    swt = models.FloatField(primary_key=True)
    usn = models.ForeignKey(StudentList, models.DO_NOTHING, db_column='usn', blank=True, null=True)
    surt = models.ForeignKey(TestSub, models.DO_NOTHING, db_column='surt', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'write_test'
