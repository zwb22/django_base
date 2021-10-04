from django.db import models

# Create your models here.


"""
1、我们的模型类需要继承自models.Model
2、系统会自动为我们添加一个主键--id
3、字段
	字段名=model.类型（选项）
	字段名其实就是数据表的字段名
	字段名不要使用python、mysql等关键字
	char(M)
	varchar(M)
	M 就是选项
"""


class BookInfo(models.Model):
	name = models.CharField(max_length=10)

	# 重写str方法以让admin来显示书籍名字
	# 将模型类以字符串的方式输出
	def __str__(self):
		return self.name


class PeopleInfo(models.Model):
	name = models.CharField(max_length=10)
	gender = models.BooleanField()
	# 外键约束：人物属于哪本书
	book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)


# 生成迁移文件，将类转换为表结构文件  python3 manage.py makemigration
# 执行迁移文件，执行表结构文件，这个时候数据库才有表 python3 manage.py migrate
