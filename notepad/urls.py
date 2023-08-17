from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("listnote/", views.NoteListView.as_view(), name="listnote")
]
