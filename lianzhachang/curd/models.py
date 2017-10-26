from django.db import models

# Create your models here.


class UserInfo(models.Model):
    """
    职工表
    """
    job_number = models.IntegerField(verbose_name='工号', unique=True)  # unique=True必须是唯一的
    name = models.CharField(verbose_name='员工姓名', max_length=16)
    age = models.IntegerField(verbose_name='年龄', blank=True)  # blank=True该字段允许为空
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.EmailField(verbose_name='邮箱', max_length=64)

    user_class_choice = (
        (1, '甲'),
        (1, '乙'),
        (1, '丙'),
        (1, '丁'),
    )
    user_class = models.IntegerField(verbose_name='班级',
                                     choices=user_class_choice, blank=True, null=True)

    education_choices = (
        (1, '博士'),
        (2, '硕士'),
        (3, '本科'),
        (4, '民办本科'),
        (5, '大专'),
        (6, '高职'),
        (7, '高中'),
        (8, '其他')
    )
    # 如果设置为null=True，Django将在数据库中将空值存储为Null,blank=True表示该字段允许为空白
    education = models.IntegerField(verbose_name='学历',
                                    choices=education_choices, blank=True, null=True)

    # 如果被关联的表在本表下面的话，类需要引号
    # 职工和作业区属于多对一关系
    operating_area = models.ForeignKey('OperatingArea')
    # 职工和职位属于多对一的关系
    position = models.ForeignKey('Position')
    # 职工和工种属于多对多的关系
    profession = models.ManyToManyField('Profession')
    # 职工和职称属于多对一的关系
    job_title = models.ForeignKey('JobTitle')
    # 职工和考核属于多对多关系
    assessment = models.ManyToManyField('Assessment')
    # 职工和奖励属于多对多关系
    reward = models.ManyToManyField('Reward')

    class Meta:
        verbose_name = '职工表'
        verbose_name_plural = verbose_name


class OperatingArea(models.Model):
    """
    作业区
    炼钢、连铸、精炼、滑板、质检、中控
    """
    title = models.CharField(verbose_name='作业区名称', max_length=16)
    area = models.CharField(verbose_name='区域', max_length=32)

    dangerous_choice = (
        (1, '高危'),
        (2, '危险'),
        (3, '小心'),
        (4, '安全'),
    )
    # 危险级别
    dangerous_level = models.IntegerField(verbose_name='危险等级',
                                          choices=dangerous_choice, blank=True, null=True)

    class Meta:
        verbose_name = '作业区表'
        verbose_name_plural = verbose_name


class Position(models.Model):
    """
    职位
    作业长、书记、安全主办、技术顾问、值班长、班长、总炉长、总机长、炉长、机长、
    第一炉长助手、第二炉长助手、工人
    """
    title = models.CharField(verbose_name='职位', max_length=32)

    class Meta:
        verbose_name = '职位表'
        verbose_name_plural = verbose_name


class Profession(models.Model):
    """
    工种
    转炉炼钢工、浇铸工、合金工、电工、钳工、天车工、
    """
    title = models.CharField(verbose_name='工种名称', max_length=32)
    retirement_age = models.IntegerField(verbose_name='退休年龄')

    class Meta:
        verbose_name = '工种表'
        verbose_name_plural = verbose_name


class JobTitle(models.Model):
    """
    职称
    助理工程师、初级工程师、中级工程师、高级工程师、教授、院士
    """
    title = models.CharField(verbose_name='职称', max_length=32)

    class Meta:
        verbose_name = '职称表'
        verbose_name_plural = verbose_name


class Assessment(models.Model):
    """
    考核表
    绩效、违章
    """
    title = models.CharField(verbose_name='考核名称', max_length=32)
    money = models.IntegerField(verbose_name='考核金额')
    date = models.DateField(verbose_name='考核时间')
    assessment_detail = models.OneToOneField('AssessmentDetail')


class AssessmentDetail(models.Model):
    """
    考核详细信息
    """
    content = models.CharField(verbose_name='考核详细信息', max_length=512)


class Reward(models.Model):
    """
    奖励
    小改小革、发明创造、提出优化、知识竞赛
    """
    title = models.CharField(verbose_name='奖励名称', max_length=32)
    money = models.IntegerField(verbose_name='奖励金额')
    date = models.DateField(verbose_name='奖励时间')
    assessment_detail = models.OneToOneField('RewardDetail')


class RewardDetail(models.Model):
    """
    奖励详细信息
    """
    content = models.CharField(verbose_name='奖励详细信息', max_length=512)


class Leave(models.Model):
    """
    休假表
    年修、轮休、探亲、产假、护理假
    """
    title = models.CharField(verbose_name='休假名称', max_length='32')
    money = models.IntegerField(verbose_name='扣款')
    begin = models.DateField(verbose_name='休假开始日期')
    end = models.DateField(verbose_name='休假结束日期')


class Wage(models.Model):
    """
    薪资表
    """
    pass
