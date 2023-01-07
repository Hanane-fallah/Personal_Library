from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .models import Book, Podcast, AudioBook, Magazine, UserLibrary, User


class Library(View):
    def get(self, request):
        books = Book.objects.all()
        audiobooks = AudioBook.objects.all()
        podcasts = Podcast.objects.all()
        magazines = Magazine.objects.all()
        context = {
            'books': books,
            'audiobooks': audiobooks,
            'podcasts': podcasts,
            'magazines': magazines
        }
        return render(request, "library/home.html", context)


class AddBook(View):
    def get(self, request, book_id):
        book_obj = Book.objects.get(id=book_id)
        user = User.objects.get(id=1)
        book_lib = UserLibrary(user=user, file=book_obj)
        book_lib.save()
        response = """
        <h4> Done </h4>
        <a href="{% url 'user_lib' 1 %}">see your library</a>
        """
        return HttpResponse(request, response)

def info(request, book_id):
    book_obj = Book.objects.get(id=book_id)
    context = {
        'book': book_obj,
    }
    return render(request, 'library/book.html', context)


class UserLib(View):
    def get(self, request, user_id):
        user_books = UserLibrary.objects.all().filter(user_id=user_id)
        books = Book.objects.all().filter(id__in=[u.id for u in user_books])
        context = {
            'user_books': user_books,
            'books': books
        }
        return render(request, 'library/library.html', context)





# def read(request, book_id):
#
#     book = Book.objects.get(id=book_id)
#
#     context = {
#         'book': book
#     }
#
#     return render(request, 'book.html', context)