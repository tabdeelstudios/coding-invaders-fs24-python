from django.urls import path

from .views import Note, AllBooks, BookById

urlpatterns = [
    path("", Note.as_view(), name="notes"),
    path("books", AllBooks.as_view(), name="books"),
    path("book/<int:id>/", BookById.as_view(), name="books")
]