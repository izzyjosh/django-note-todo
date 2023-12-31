from django.urls import path
from . import views

urlpatterns = [
    path("listnote/", views.NoteListView.as_view(), name="index"),
    path("detailnote/<int:pk>",views.NoteDetailView.as_view(), name="detail"),
    path("createnote/", views.createnote, name="createnote"), 
    path("delete/<int:note_id>/", views.delete, name="delete"),
    path("update/<int:note_id>/", views.update, name="update"), 

]
