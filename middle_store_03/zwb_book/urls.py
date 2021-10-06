from django.urls import path
import zwb_book.views as views

urlpatterns = [
    path('zwb/', views.create_book),
]
