# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 09:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=160, null=True, unique=True)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_group',
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_group_permissions',
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=510, null=True)),
                ('codename', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_permission',
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=256, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(blank=True, max_length=300, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=60, null=True)),
                ('last_name', models.CharField(blank=True, max_length=60, null=True)),
                ('email', models.CharField(blank=True, max_length=508, null=True)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user_groups',
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user_user_permissions',
            },
        ),
        migrations.CreateModel(
            name='CamsLogin',
            fields=[
                ('userid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'cams_login',
            },
        ),
        migrations.CreateModel(
            name='ClassTchr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=1)),
                ('sem', models.BooleanField()),
                ('year', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'class_tchr',
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(blank=True, max_length=400, null=True)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'django_admin_log',
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app_label', models.CharField(blank=True, max_length=200, null=True)),
                ('model', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'django_content_type',
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(blank=True, max_length=510, null=True)),
                ('name', models.CharField(blank=True, max_length=510, null=True)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_migrations',
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('session_data', models.TextField(blank=True, null=True)),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_session',
            },
        ),
        migrations.CreateModel(
            name='FacultyEnr',
            fields=[
                ('eno', models.FloatField(primary_key=True, serialize=False)),
                ('slot', models.BooleanField()),
                ('day', models.CharField(max_length=3)),
                ('section', models.CharField(max_length=1)),
                ('year', models.IntegerField()),
                ('sem', models.BooleanField()),
            ],
            options={
                'managed': False,
                'db_table': 'faculty_enr',
            },
        ),
        migrations.CreateModel(
            name='FacultyResponsibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsibility', models.CharField(max_length=10)),
            ],
            options={
                'managed': False,
                'db_table': 'faculty_responsibility',
            },
        ),
        migrations.CreateModel(
            name='FrontendModule',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('label', models.CharField(blank=True, max_length=100, null=True)),
                ('installed', models.BooleanField()),
            ],
            options={
                'managed': False,
                'db_table': 'frontend_module',
            },
        ),
        migrations.CreateModel(
            name='StudentAtt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dte', models.DateField()),
            ],
            options={
                'managed': False,
                'db_table': 'student_att',
            },
        ),
        migrations.CreateModel(
            name='StudentClassenr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'student_classenr',
            },
        ),
        migrations.CreateModel(
            name='StudentSemenr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=2)),
                ('sem', models.BooleanField()),
                ('section', models.CharField(max_length=1)),
            ],
            options={
                'managed': False,
                'db_table': 'student_semenr',
            },
        ),
        migrations.CreateModel(
            name='SubjectList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scode', models.CharField(max_length=8)),
                ('sname', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=2)),
            ],
            options={
                'managed': False,
                'db_table': 'subject_list',
            },
        ),
        migrations.CreateModel(
            name='TestId',
            fields=[
                ('tid', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('slot', models.CharField(max_length=1)),
                ('branch', models.CharField(max_length=2)),
                ('sem', models.CharField(blank=True, max_length=1, null=True)),
                ('tno', models.NullBooleanField()),
            ],
            options={
                'managed': False,
                'db_table': 'test_id',
            },
        ),
        migrations.CreateModel(
            name='WriteTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'write_test',
            },
        ),
        migrations.CreateModel(
            name='FacultyList',
            fields=[
                ('fid', models.ForeignKey(db_column='fid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='clsteacher.CamsLogin')),
                ('name', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=30)),
                ('branch', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'faculty_list',
            },
        ),
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('usn', models.ForeignKey(db_column='usn', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='clsteacher.CamsLogin')),
                ('name', models.CharField(max_length=30)),
                ('joining', models.DateField()),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('phno', models.CharField(max_length=15)),
                ('parent_phno', models.CharField(max_length=15)),
            ],
            options={
                'managed': False,
                'db_table': 'student_list',
            },
        ),
        migrations.CreateModel(
            name='TestNo',
            fields=[
                ('tid', models.ForeignKey(db_column='tid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='clsteacher.TestId')),
                ('scode', models.CharField(max_length=8)),
            ],
            options={
                'managed': False,
                'db_table': 'test_no',
            },
        ),
    ]
