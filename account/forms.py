from django import forms
from django.contrib.auth.forms import PasswordResetForm


class MyPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget = forms.EmailInput(attrs={
            "class": "user_data",
            "placeholder": "email",
        })
        self.fields["email"].label = False
