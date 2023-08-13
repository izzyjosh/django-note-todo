from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("createnote/", views.create, name="create_note.html")
]
