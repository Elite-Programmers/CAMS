# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Att',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sur8', models.FloatField(blank=True, null=True)),
                ('year', models.DateField(blank=True, null=True)),
                ('slot', models.CharField(blank=True, max_length=1, null=True)),
                ('scode', models.CharField(blank=True, max_length=8, null=True)),
                ('day', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'db_table': 'att',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FacEnr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sur7', models.FloatField(blank=True, null=True)),
                ('fid', models.CharField(blank=True, max_length=7, null=True)),
                ('slot', models.CharField(blank=True, max_length=1, null=True)),
                ('day', models.CharField(blank=True, max_length=3, null=True)),
                ('section', models.CharField(max_length=1)),
                ('branch', models.CharField(blank=True, max_length=2, null=True)),
                ('year', models.FloatField(blank=True, null=True)),
                ('scode', models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                'db_table': 'fac_enr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentSubEnr',
            fields=[
                ('sur3', models.FloatField(primary_key=True, serialize=False)),
                ('scode', models.CharField(blank=True, max_length=8, null=True)),
                ('sname', models.CharField(blank=True, max_length=50, null=True)),
                ('branch', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 'student_sub_enr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestSub',
            fields=[
                ('sur5', models.FloatField(primary_key=True, serialize=False)),
                ('tno', models.FloatField(blank=True, null=True)),
                ('scode', models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                'db_table': 'test_sub',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestTme',
            fields=[
                ('sur4', models.FloatField(primary_key=True, serialize=False)),
                ('tno', models.FloatField(blank=True, null=True)),
                ('dte', models.DateField(blank=True, null=True)),
                ('slot', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'test_tme',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='studentsemenr',
            table='student_sem_enr',
        ),
    ]
