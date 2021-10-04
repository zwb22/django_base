from django.urls import path
from zwb_book.views import index


urlpatterns = {
	path('index/', index)
}