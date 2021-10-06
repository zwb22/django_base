from django.http import HttpResponse
from django.shortcuts import render
from zwb_book.models import BookInfo


def create_book(p_request):
	p_book_info = BookInfo.objects.create(
		book_name='zwb1',
		pub_date='1996-09-12',
		read_count=100,
	)
	return HttpResponse('0dw')
