from django.shortcuts import render
from django.db.models import Q
from .models import Note


def index(request):
    search = request.GET.get("search", "")
    cat = request.GET.get("category", "")

    note = Note.objects.filter(
        Q(title__icontains=search) |
        Q(body__icontains=search) |
        Q(category__name=cat),
        owner=request.user
    )
    context = {
        "note": note
    }

    return render(request, "index.html", context)


def create(request):
    return render(request, "create_note.html")
