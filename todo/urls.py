from django.urls import path 
from . import views

urlpatterns = [
        path("todo/", views.todos, name="todo"), 
        path("delete/<int:todo_id>/", views.delete, name="delete"), 
        ]
