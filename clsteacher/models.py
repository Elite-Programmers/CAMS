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
    satt = models.FloatField(blank=True, null=True)
    usn = models.ForeignKey('StudentList', models.DO_NOTHING, db_column='usn', blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    slot = models.FloatField(blank=True, null=True)
    scode = models.CharField(max_length=8, blank=True, null=True)
    day = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=160, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=510, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=256, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=300, blank=True, null=True)
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=508, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=400, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=510, blank=True, null=True)
    name = models.CharField(max_length=510, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=80)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FacEnr(models.Model):
    sfid = models.FloatField(blank=True, null=True)
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


class FrontendModule(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    label = models.CharField(max_length=100, blank=True, null=True)
    installed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'frontend_module'


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
