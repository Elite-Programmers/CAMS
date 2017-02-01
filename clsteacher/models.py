# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


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
    fid = models.ForeignKey('FacultyList', models.DO_NOTHING, db_column='fid')
    section = models.CharField(max_length=1)
    sem = models.BooleanField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'class_tchr'
        unique_together = (('fid', 'sem', 'year'),)


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


class FrontendModule(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    label = models.CharField(max_length=100, blank=True, null=True)
    installed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'frontend_module'


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
