from django.urls import path

from .views import Note

urlpatterns = [
    path("", Note.as_view(), name="notes")
]