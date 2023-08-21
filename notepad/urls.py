from django.urls import path
from . import views

urlpatterns = [
    path("listnote/", views.NoteListView.as_view(), name="index"),
    path("derailnote/<int:pk>",views.NoteDetailView.as_view(), name="detail"), 
]
