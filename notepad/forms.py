from django import forms
from notepad.models import Note


CATEGORY = [
        ("education", "educational"), 
        ("personal", "personal"), 
        ("work", "work")
        ]

class Addform(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("title", "body", "category")

        widget = {
                "title":forms.TextInput(attrs=
                {
                    "class":"form_input", 
                    "name":"title", 
                    "placeholder":"title", 
                    "id":"title"
                }),
                "body":forms.Textarea(attrs={
                    "class":"body-note", 
                    "name":"body", 
                    "placeholder":"body of your note",}),}

                
