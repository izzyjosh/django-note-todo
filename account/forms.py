from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class MyPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget = forms.EmailInput(attrs={
            "class": "user_data",
            "placeholder": "email",
        })
        self.fields["email"].label = False


class MySetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].widget = forms.PasswordInput(attrs={
            "class": "user_data",
            "placeholder": "New Password"
        })
        self.fields["new_password1"].label = False
        self.fields["new_password2"].widget = forms.PasswordInput(attrs={
            "class": "user_data",
            "placeholder": "Confirm New Password"
        })
        self.fields["new_password2"].label = False
