from django.urls import path

from library import views

urlpatterns = [
    path('mylibrary/', views.user_library),
    ]