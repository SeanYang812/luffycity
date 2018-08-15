# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-10 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='章节')),
                ('name', models.CharField(max_length=32, verbose_name='章节名称')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Course', verbose_name='所属课程')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_sections', to='app01.Chapter')),
            ],
            options={
                'verbose_name_plural': '11. 课时',
            },
        ),
        migrations.CreateModel(
            name='OftenAskedQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField(max_length=1024)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': '08. 常见问题',
            },
        ),
        migrations.AlterUniqueTogether(
            name='oftenaskedquestion',
            unique_together=set([('content_type', 'object_id', 'question')]),
        ),
    ]