from django.urls import path
from . import views

urlpatterns = [
    path("listnote/", views.NoteListView.as_view(), name="index"), 
]
