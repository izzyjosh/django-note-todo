from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Note
from django.views.generic import ListView
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
        
