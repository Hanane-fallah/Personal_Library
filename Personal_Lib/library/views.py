from django.http import HttpResponse
from django.shortcuts import render, redirect

from library.models import Book, Podcast, AudioBook, Magazine, UserLibrary, User


def home(request):
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
    if request.method == "POST":
        book_id = request.POST['add_book']
        book_obj = Book.objects.get(id=book_id)
        user = User.objects.get(id=1)
        book_lib = UserLibrary(user=user, file=book_obj)
        book_lib.save()
        print('done')
        return user_library(request)

    return render(request, 'home.html', context)


def user_library(request):
    user_books = UserLibrary.objects.all().filter(user_id=1)
    books = Book.objects.all().filter(id__in=[u.id for u in user_books])
    context = {
        'books': books
    }
    # if request.method == "POST":
    #     book_id = request.POST['book_id']
    #     book = Book.objects.get(id=book_id.id)
    #     read(book, 5)

    return render(request, 'library.html', context)


