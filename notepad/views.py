from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Note, Category
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from notepad.forms import Addform
from django.contrib.auth.mixins import LoginRequiredMixin



class NoteListView(LoginRequiredMixin, ListView):

    template_name = "index.html"
    login_url = "signin"

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


class NoteDetailView(LoginRequiredMixin, DetailView):
       template_name = "detail.html"
       login_url = "signin"
       model = Note
       context_object_name = "note"


def createnote(request):
    if request.method == "POST":

        title = request.POST['title']
        body = request.POST['body']
        category = request.POST['category']

        category, _ = Category.objects.get_or_create(
                name__icontains=category, 
                name=category
        )

        Note.objects.create(
                title=title, 
                body=body, 
                category=category, 
                owner=request.user)

        return redirect("index")
    category = Category.objects.all()
        
    context = {
            "categories":category, 
            }

    return render(request, "create_note.html", context)


def delete(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()
    return redirect("index")


