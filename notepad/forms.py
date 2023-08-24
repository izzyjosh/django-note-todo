from django import forms
from notepad.models import Note


class Addform(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("title", "body", "category")

        widget = {
                "title":forms.TextInput(attrs=
                {
                    "class":"title", 
                    "type":"text", 
                    "name":"title", 
                    "placeholder":"title", 
                    "id":"title", 
                }),
                "body":forms.Textarea(attrs={
                    "class":"body", 
                    "name":"body", 
                    "placeholder":"body", 
                    }), 
                "category":forms.Select(attrs={
                    "class":"cat", 
                    "name": "category"
                    })
                }

                
