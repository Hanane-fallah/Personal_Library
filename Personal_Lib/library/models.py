from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


#  todo:   get_absolute_url - str - save
# class Meta: # new
#         indexes = [models.Index(fields=["full_name"])]
#         ordering = ["-full_name"]
#         verbose_name = "university"
#         verbose_name_plural = "universities"

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    death = models.DateField(blank=True, null=True)

    # todo: description txt
    def __str__(self):
        return f"{self.name} - {self.birthday} : {self.death or '-'}"


class Language(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.country}"


class BaseBookClass(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name="book_author")
    publish_year = models.IntegerField()
    pages = models.IntegerField()
    book_language = models.ManyToManyField(Language, related_name="book_language")
    price = models.FloatField()
    file = models.FileField(upload_to='files')

    # todo: description txt

    class Meta:
        abstract = True


class Book(BaseBookClass):
    authors = models.ManyToManyField(Author, related_name="book_author")

    def __str__(self):
        return f"{self.title} - {self.publish_year}"


class Magazine(BaseBookClass):
    authors = models.ManyToManyField(Author, related_name="magazine_author")
    book_language = models.ManyToManyField(Language, related_name="magazine_language")
    issue = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} : {self.issue} - {self.publish_year}"


class AudioBook(BaseBookClass):
    authors = models.ManyToManyField(Author, related_name="Abook_author")
    book_language = models.ManyToManyField(Language, related_name="audiobook_language")
    speaker = models.CharField(max_length=100)
    audio_language = models.ForeignKey(Language, default="Unknown", on_delete=models.SET_DEFAULT,
                                       related_name="audio_language")
    time = models.TimeField()

    def __str__(self):
        return f"{self.title} - {self.publish_year} : {self.time}"


class Podcast(models.Model):
    title = models.CharField(max_length=100)
    speaker = models.CharField(max_length=100)
    publish_year = models.IntegerField()
    time = models.TimeField()
    audio_language = models.ForeignKey(Language, default="Unknown", on_delete=models.SET_DEFAULT)
    price = models.FloatField()
    file = models.FileField(upload_to='files')

    # todo: description txt

    def __str__(self):
        return f"{self.title} - {self.speaker} : {self.time}"


class UserLibrary(models.Model):
    book_status = [
        ('unread', 'unread'),
        ('reading', 'reading'),
        ('finished', 'finished')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    file = models.ForeignKey(Book, on_delete=models.CASCADE, unique=True)
    status = models.CharField(max_length=10, choices=book_status, default='unread')
    status_value = models.IntegerField(default=0)
