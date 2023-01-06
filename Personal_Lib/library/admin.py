from django.contrib import admin

from .models import Book, AudioBook, Magazine, Podcast, User, Language, Author, UserLibrary

# Register your models here.
admin.site.register(Book)
admin.site.register(AudioBook)
admin.site.register(Magazine)
admin.site.register(Podcast)
admin.site.register(User)
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(UserLibrary)
