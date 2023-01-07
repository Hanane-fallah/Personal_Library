from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.Library.as_view(), name='show_library'),
    path('addbook/<int:book_id>', views.AddBook.as_view(), name='add_book'),
    path('mylib/<int:user_id>', views.UserLib.as_view(), name="user_lib"),
    path('info/<int:book_id>', views.info, name="book_info"),
    path('read/<int:book_id>', views.read, name="book_read"),

    ]