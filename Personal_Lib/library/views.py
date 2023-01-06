from django.http import HttpResponse
from django.shortcuts import render

from library.models import Book, Podcast, AudioBook, Magazine, UserLib, User



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
        book_lib = UserLib(user_id=user, file=book_obj)
        book_lib.save()
        return HttpResponse("added to lib")

    return render(request, 'home.html', context)
