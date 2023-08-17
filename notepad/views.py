from django.shortcuts import render
from django.db.models import Q
from .models import Note
from django.views.generic import ListView

def index(request):
    search = request.GET.get("search", "")
    cat = request.GET.get("category", "")

    notes = Note.objects.filter(
        Q(title__icontains=search) |
        Q(body__icontains=search) |
        Q(category__name=cat),
        owner=request.user
    )
    context = {
        "notes": notes
    }

    return render(request, "index.html", context)


class NoteListView(ListView):
    template_name = "index.html"

    def get_queryset(self):
        search = self.request.GET.get("search", "")
        cat = self.request.GET.get("category", "")

        self.notes = Note.objects.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search) | 
                Q(category__name=cat), 
                owner=self.request.user)
        return self.notes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notes"] = self.notes
        return context



#def create(request):
    #return render(request, "create_note.html")
