from django.contrib import admin
from .models import *


class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "body", "date", )
admin.site.register(Note, NoteAdmin)


admin.site.register(Category)
