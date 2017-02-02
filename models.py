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
    sur8 = models.FloatField(blank=True, null=True)
    usn = models.ForeignKey('StudentList', models.DO_NOTHING, db_column='usn', blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    slot = models.CharField(max_length=1, blank=True, null=True)
    scode = models.CharField(max_length=8, blank=True, null=True)
    day = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att'
        unique_together = (('usn', 'year', 'slot'),)


class CamsLogin(models.Model):
    userid = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cams_login'


class ClassTchr(models.Model):
    sfid = models.FloatField(primary_key=True)
    fid = models.ForeignKey('FacultyList', models.DO_NOTHING, db_column='fid', blank=True, null=True)
    section = models.CharField(max_length=1)
    sem = models.FloatField(blank=True, null=True)
    year = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_tchr'
        unique_together = (('fid', 'sem', 'year'),)


class FacEnr(models.Model):
    sur7 = models.FloatField(blank=True, null=True)
    fid = models.CharField(max_length=7, blank=True, null=True)
    slot = models.CharField(max_length=1, blank=True, null=True)
    day = models.CharField(max_length=3, blank=True, null=True)
    section = models.CharField(max_length=1)
    branch = models.CharField(max_length=2, blank=True, null=True)
    year = models.FloatField(blank=True, null=True)
    scode = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fac_enr'
        unique_together = (('fid', 'slot', 'day', 'year'),)


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
    sem = models.FloatField(blank=True, null=True)
    branch = models.CharField(max_length=4, blank=True, null=True)
    year_of_joining = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    parent_phno = models.BigIntegerField(blank=True, null=True)
    phno = models.BigIntegerField(blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_list'


class StudentSemEnr(models.Model):
    sur2 = models.FloatField(primary_key=True)
    usn = models.ForeignKey(StudentList, models.DO_NOTHING, db_column='usn', blank=True, null=True)
    branch = models.CharField(max_length=2, blank=True, null=True)
    sem = models.FloatField(blank=True, null=True)
    batch = models.FloatField(blank=True, null=True)
    section = models.CharField(max_length=1, blank=True, null=True)
    year = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_sem_enr'
        unique_together = (('usn', 'sem', 'section', 'year'),)


class StudentSubEnr(models.Model):
    sur3 = models.FloatField(primary_key=True)
    scode = models.CharField(max_length=8, blank=True, null=True)
    sname = models.CharField(max_length=50, blank=True, null=True)
    branch = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_sub_enr'
        unique_together = (('scode', 'branch'),)


class TestSub(models.Model):
    sur5 = models.FloatField(primary_key=True)
    tno = models.FloatField(blank=True, null=True)
    scode = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_sub'
        unique_together = (('tno', 'scode'),)


class TestTme(models.Model):
    sur4 = models.FloatField(primary_key=True)
    tno = models.FloatField(blank=True, null=True)
    dte = models.DateField(blank=True, null=True)
    slot = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_tme'
        unique_together = (('tno', 'dte', 'slot'),)


class WriteTest(models.Model):
    sur6 = models.FloatField(primary_key=True)
    usn = models.ForeignKey(StudentList, models.DO_NOTHING, db_column='usn', blank=True, null=True)
    surt = models.ForeignKey(TestSub, models.DO_NOTHING, db_column='surt', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'write_test'
        unique_together = (('usn', 'score'),)
