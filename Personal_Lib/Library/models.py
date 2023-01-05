from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


#     get_absolute_url - str - save
# class Meta: # new
#         indexes = [models.Index(fields=["full_name"])]
#         ordering = ["-full_name"]
#         verbose_name = "university"
#         verbose_name_plural = "universities"

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.birthday} : {self.death or '-'}"


class Language(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.country}"


class BaseBookClass(models.Model):
    title = models.CharField(max_length=100, default="Unknown")
    authors = models.ManyToManyField(Author, related_name="book_author")
    publish_year = models.IntegerField(default="Unknown")
    pages = models.IntegerField(default="Unknown")
    book_language = models.ManyToManyField(Language)
    price = models.FloatField(default="Unknown")

    class Meta:
        abstract = True


class Book(BaseBookClass):
    authors = models.ManyToManyField(Author, related_name="book_author")

    def __str__(self):
        return f"{self.title} - {self.publish_year}"


class Magazine(BaseBookClass):
    authors = models.ManyToManyField(Author, related_name="magazine_author")
    issue = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} : {self.issue} - {self.publish_year}"


class AudioBook(BaseBookClass):
    authors = models.ManyToManyField(Author, related_name="Abook_author")
    speaker = models.CharField(max_length=100)
    audio_language = models.ForeignKey(Language, default="Unknown", on_delete=models.SET_DEFAULT,
                                       related_name="audio_language")
    time = models.TimeField(default="Unknown")

    def __str__(self):
        return f"{self.title} - {self.publish_year} : {self.time}"


class Podcast(models.Model):
    title = models.CharField(max_length=100, default="Unknown")
    speaker = models.CharField(max_length=100, default="Unknown")
    publish_year = models.IntegerField(default="Unknown")
    time = models.TimeField(default="Unknown")
    audio_language = models.ForeignKey(Language, default="Unknown", on_delete=models.SET_DEFAULT)
    price = models.FloatField(default="Unknown")

    def __str__(self):
        return f"{self.title} - {self.speaker} : {self.time}"
