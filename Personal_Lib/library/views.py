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
        return redirect('show_library')


class UserLib(View):
    def get(self, request, user_id):
        user_books = UserLibrary.objects.all().filter(user_id=user_id)
        books = Book.objects.all().filter(id__in=[u.file_id for u in user_books])
        context = {
            'user_books': user_books,
            'books': books
        }
        return render(request, 'library/library.html', context)


class Read(View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        user_book = UserLibrary.objects.get(file_id=book_id)
        context = {
            'book': book,
            'user_book': user_book
        }
        return render(request, 'library/book.html', context)

    def post(self, request, book_id):
        page_num = request.POST['current_page']
        user_book = UserLibrary.objects.get(file_id=book_id)
        user_book.status_value += int(page_num)
        book = Book.objects.get(id=book_id)

        if user_book.status_value == 0:
            user_book.status = 'unread'

        elif user_book.status_value == book.pages:
            user_book.status = 'finished'

        elif user_book.status_value <= book.pages:
            user_book.status = 'reading'

        user_book.save()
        user_book = UserLibrary.objects.get(file_id=book_id)
        context = {
            'book': book,
            'user_book': user_book
        }
        return render(request, 'library/book.html', context)


def info(request, book_id):
    book_obj = Book.objects.get(id=book_id)
    context = {
        'book': book_obj,
    }
    return render(request, 'library/book_info.html', context)

