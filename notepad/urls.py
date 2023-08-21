from django.urls import path
from . import views

urlpatterns = [
    path("listnote/", views.NoteListView.as_view(), name="index"),
    path("detailnote/<int:pk>",views.NoteDetailView.as_view(), name="detail"),
    path("createnote/", views.createnote, name="createnote"), 
]
