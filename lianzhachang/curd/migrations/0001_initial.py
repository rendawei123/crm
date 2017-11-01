# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 07:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='考核名称')),
                ('money', models.IntegerField(verbose_name='考核金额')),
                ('date', models.DateField(verbose_name='考核时间')),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=512, verbose_name='考核详细信息')),
            ],
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='职称')),
            ],
            options={
                'verbose_name': '职称表',
                'verbose_name_plural': '职称表',
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='休假名称')),
                ('money', models.IntegerField(verbose_name='扣款')),
                ('begin', models.DateField(verbose_name='休假开始日期')),
                ('end', models.DateField(verbose_name='休假结束日期')),
            ],
        ),
        migrations.CreateModel(
            name='OperatingArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, verbose_name='作业区名称')),
                ('area', models.CharField(max_length=32, verbose_name='区域')),
                ('dangerous_level', models.IntegerField(blank=True, choices=[(1, '高危'), (2, '危险'), (3, '小心'), (4, '安全')], null=True, verbose_name='危险等级')),
            ],
            options={
                'verbose_name': '作业区表',
                'verbose_name_plural': '作业区表',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='职位')),
            ],
            options={
                'verbose_name': '职位表',
                'verbose_name_plural': '职位表',
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='工种名称')),
                ('retirement_age', models.IntegerField(verbose_name='退休年龄')),
            ],
            options={
                'verbose_name': '工种表',
                'verbose_name_plural': '工种表',
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='奖励名称')),
                ('money', models.IntegerField(verbose_name='奖励金额')),
                ('date', models.DateField(verbose_name='奖励时间')),
            ],
        ),
        migrations.CreateModel(
            name='RewardDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=512, verbose_name='奖励详细信息')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_number', models.IntegerField(unique=True, verbose_name='工号')),
                ('name', models.CharField(max_length=16, verbose_name='员工姓名')),
                ('age', models.IntegerField(blank=True, verbose_name='年龄')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('email', models.EmailField(max_length=64, verbose_name='邮箱')),
                ('user_class', models.IntegerField(blank=True, choices=[(1, '甲'), (1, '乙'), (1, '丙'), (1, '丁')], null=True, verbose_name='班级')),
                ('education', models.IntegerField(blank=True, choices=[(1, '博士'), (2, '硕士'), (3, '本科'), (4, '民办本科'), (5, '大专'), (6, '高职'), (7, '高中'), (8, '其他')], null=True, verbose_name='学历')),
                ('assessment', models.ManyToManyField(to='curd.Assessment')),
                ('job_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curd.JobTitle')),
                ('leave', models.ManyToManyField(to='curd.Leave')),
                ('operating_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curd.OperatingArea')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curd.Position')),
                ('profession', models.ManyToManyField(to='curd.Profession')),
                ('reward', models.ManyToManyField(to='curd.Reward')),
            ],
            options={
                'verbose_name': '职工表',
                'verbose_name_plural': '职工表',
            },
        ),
        migrations.CreateModel(
            name='Wage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_money', models.IntegerField(verbose_name='工资总额')),
                ('basic_money', models.IntegerField(verbose_name='基本工资')),
                ('performance', models.IntegerField(verbose_name='绩效工资')),
            ],
        ),
        migrations.CreateModel(
            name='WageDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_insurance', models.IntegerField(verbose_name='医疗保险')),
                ('unemployment_insurance', models.IntegerField(verbose_name='失业保险')),
                ('injury_insurance', models.IntegerField(verbose_name='工伤保险')),
                ('pension', models.IntegerField(verbose_name='养老保险')),
                ('housing_fund', models.IntegerField(verbose_name='住房公积金')),
                ('leave_money', models.IntegerField(verbose_name='休假扣款')),
                ('reward_money', models.IntegerField(verbose_name='奖金')),
            ],
        ),
        migrations.AddField(
            model_name='wage',
            name='wage_detail',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='curd.WageDetail'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='wage',
            field=models.ManyToManyField(to='curd.Wage'),
        ),
        migrations.AddField(
            model_name='reward',
            name='assessment_detail',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='curd.RewardDetail'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='assessment_detail',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='curd.AssessmentDetail'),
        ),
    ]
