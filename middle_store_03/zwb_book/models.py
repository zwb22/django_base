from django.db import models

# Create your models here.
"""
1、模型类 需要继承自models.Model
2、定义属性
	id 系统默认会生成
	属性名=models.类型（选项）
	2.1 属性名 对应 就是字段名
		不要使用python、mysql关键字
		不要使用连续的下划线（__）
	2.2 类型 mysql的类型
	2.3 选项 是否有默认值，是否唯一，是否为null
			CharField 必须设置max_length
3、 改变表的名称
	默认表的名称是: 子应用名_类名 都是小写
	修改表的名字 
create table `qq_user` (
	id int ,
	name varchar(10) not null default ''

"""


class BookInfo(models.Model):
	# 书籍名
	book_name = models.CharField(max_length=10, unique=True)
	# 发布日期
	pub_date = models.DateField(null=True)
	# 阅读量
	read_count = models.IntegerField(default=0)
	# 评论数
	comment_count = models.IntegerField(default=0)
	# 是否下架
	is_delete = models.BooleanField(default=False)

	# 隐藏的系统生成的级联字段(一对多的模型中，系统会为我们自动添加一个关联模型类名小写_set)
	# peopleinfo_set = [PeopleInfo, PeopleInfo,...]

	class Meta:
		# 修改表的名字
		db_table = 'bookinfo'
		# admin站点使用的（了解）
		verbose_name = '书籍管理'

	def __str__(self):
		return self.book_name


class PeopleInfo(models.Model):
	# 人物名
	people_name = models.CharField(max_length=10, unique=True)

	# 定义一个有序字典
	GENDER_CHOICE = {
		(1, 'male'),
		(2, 'female'),
	}
	# 性别
	gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)

	# 描述信息
	description = models.CharField(max_length=100, null=True)
	# 是否下架
	is_delete = models.BooleanField(default=False)

	# 所属书籍id(外键)
	# 系统会自动为外键添加_id	- book_id
	"""
	外键的级联操作 - 主表的一条数据删除了，从表有关联的数据 怎么办？
	1、SET_NUILL
	2、抛出异常，不让删除
	3、级联删除
	"""
	book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

	class Meta:
		db_table = 'peopleinfo'

	def __str__(self):
		return self.people_name
