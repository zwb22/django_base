from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from zwb_book.models import BookInfo
from zwb_book.models import PeopleInfo


def index(p_request):

	# 在这里实现数据库的增删改查
	books = BookInfo.objects.all()
	print(books)
	return HttpResponse('zwb')


# 该函数为学习函数
def study_test():
	# -----------------------增加数据-----------------------
	# 方式一 - 必须调用save方法才能将数据保存到数据库中
	p_book_info = BookInfo(book_name='django', pub_date='2021-1-1', read_count=10)
	p_book_info.save()
	# 方式二 - objects -- 相当于一个代理 帮我们实现增删改查
	BookInfo.objects.create(book_name='flask', pub_date='2021-1-1', read_count=10)
	# -----------------------修改数据-----------------------
	# 方式一 - 想要保存数据 需要调用对象的save方法
	# 相当于查询语句 select * from bookinfo where id=6
	p_book_get = BookInfo.objects.get(id=8)
	p_book_get.book_name = '运维开发入门'
	p_book_get.save()
	# 方式二 - filter 过滤
	BookInfo.objects.filter(id=8).update(book_name='zwb', comment_count=666)
	# -----------------------删除数据-----------------------
	# 方式一 -删除分两种 - 物理删除（这条记录的数据删除）和 逻辑删除（修改标记位，如is_delete=False）
	p_book_del = BookInfo.objects.get(id=8)
	p_book_del.delete()
	# 方式二
	BookInfo.objects.filter(id=5).delete()
	# -----------------------查询数据-----------------------
	# get - 查询单一结果，如果不存在会抛出异常-模型类.DoesNotExist
	try:
		p_book_get_one = BookInfo.objects.get(id=99)
	except BookInfo.DoesNotExist:
		print(f'error-查询结果不存在')
	# all - 查询多个结果
	p_book_get_all = BookInfo.objects.all()
	# count - 查询结果数量
	i_book_record_count_1 = BookInfo.objects.count()
	i_book_record_count_2 = BookInfo.objects.all().count()
	# ----------------------过滤查询
	# filter过滤出多个结果
	# exclude排除掉符合条件剩下的结果
	# get 过滤单一结果

	# 模型类名.objects.filter(属性名__运算符=值) 获取n个结果 n=0,1,2,3...
	# 模型类名.objects.exclude(属性名__运算符=值) 获取n个结果 n=0,1,2,3...
	# 模型类名.objects.get(属性名__运算符=值) 获取1个结果 或者 异常

	# 查询编号为1的图书
	# 完整模式
	BookInfo.objects.get(id__exact=1)
	# 简写模式
	BookInfo.objects.get(id=1)
	# pk = primary key = 主键
	BookInfo.objects.get(pk=1)
	BookInfo.objects.filter(id=1)

	# 查询书名包含"湖"的图书
	BookInfo.objects.filter(book_name__contains='湖')

	# 查询书名以'部'结尾的图书
	BookInfo.objects.filter(book_name__endswith='部')

	# 查询书名为空的图书
	BookInfo.objects.filter(book_name__isnull=True)

	# 查询编号为1、3、5的图书
	BookInfo.objects.filter(id__in=(1, 3, 5))

	# 查询编号大于3的图书
	# 大于-gt,大于等于-gte,小于-lt,小于等于-lte
	BookInfo.objects.filter(id__gt=3)
	# 查询编号不等于3的图书
	BookInfo.objects.exclude(id=3)

	# 查询1980年发表的图书
	BookInfo.objects.filter(pub_date__year=1980)

	# 查询1990年1月1号后发表的图书
	BookInfo.objects.filter(pub_date__gt='1990-1-1')

	from django.db.models import F
	# 查询阅读量大于2倍评论量的图书 - 2个属性的比较 - TODO F对象
	BookInfo.objects.filter(read_count__gte=F('comment_count')*2)

	# 并且查询
	# 查询阅读量大于20且编号小于3的图书
	BookInfo.objects.filter(read_count__gt=20, id__lt=3)

	# 或者查询 TODO Q对象
	from django.db.models import Q
	# 查询阅读量大于20或编号小于3的图书
	BookInfo.objects.filter(Q(read_count__gt=20) | Q(id__lt=3))
	# 非查询 - 获取编号不为3的图书
	BookInfo.objects.filter(~Q(id=3))

	# 聚合函数
	from django.db.models import Sum, Max, Min, Avg, Count
	BookInfo.objects.aggregate(Sum('read_count'))

	# todo 排序函数
	# 升序
	BookInfo.objects.all().order_by('read_count')
	# 降序
	BookInfo.objects.all().order_by('-read_count')

	# todo 关联查询 - 2个表级联操作
	# 查询书籍为1的所有人物信息
	p_book_obj = BookInfo.objects.get(id=1)
	p_book_obj.peopleinfo_set.all()

	# 查询人物为1的书籍信息
	p_person_obj = PeopleInfo.objects.get(id=1)
	p_person_obj.book.book_name

	# 关联过滤查询
	# 查询图书，要求图书人物为郭靖
	BookInfo.objects.filter(peopleinfo__people_name='郭靖')
	# 查询图书，要求图书中人物描述包含"八"
	BookInfo.objects.filter(peopleinfo__description__contains='八')

	# 查询书名为"天龙八部"的所有人物
	PeopleInfo.objects.filter(book__book_name='天龙八部')
	# 查询图书阅读量大于30的所有人物
	PeopleInfo.objects.filter(book__read_count__gt=30)

	# todo 查询结果集QuerySet - 两大特性 1、惰性执行 2、缓存
	# 1、惰性执行 用变量来接收,如p
	p = BookInfo.objects.filter(id=1)
	# 2、缓存 - mysql的数据存储在硬盘，redis的数据存储在内存，把硬盘的数据存储在内存也称之为缓存
	[p_book.id for p_book in BookInfo.objects.all()]
	# 以上为不建议写法，以下直接读取缓存,多次查询性能高
	p_book_all = BookInfo.objects.all()
	[p_book_one.id for p_book_one in p_book_all]









