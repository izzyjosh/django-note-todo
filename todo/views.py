from django.shortcuts import render, redirect
from .models import Todo

def todos(request):
    if request.method == "POST":
        todo = request.POST['subject']

        Todo.objects.create(owner=request.user, subject=todo)

    todo = Todo.objects.filter(owner=request.user)

    context = {"todos":todo}

    return render(request, "todo.html", context)

def delete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('todo')

