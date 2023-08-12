from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class ResetPasswordForm(PasswordResetForm):
    """ Custom PasswordResetForm """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    email = forms.EmailField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={
            "name": "email",
            "type": "email",
            "id": "email",
            "placeholder": "Email"
        })
    )

    class Meta:
        model = User
        fields = ("email",)


class SetNewPasswordForm(SetPasswordForm):
    """ Custom SetPasswordForm """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    new_password1 = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(attrs={
            "type": "password",
            "name": "new_password1",
            "placeholder": "Password"
        })
    )

    new_password2 = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(attrs={
            "type": "password",
            "name": "new_password2",
            "placeholder": "Confirm Password"
        })
    )

    class Meta:
        model = User
        fields = ("new_password1", "new_password2")

    def clean_new_password1(self, *args, **kwargs):
        symbols = "@#_~[]{}()$&?%/"
        password = self.cleaned_data.get("new_password1")

        # MinimumLengthValidator
        if len(password) < 10:
            raise forms.ValidationError(
                "Password is too short. Requires a minimum of 10 characters")

        # CommonPasswordValidator
        if password.isdigit() or password.isalpha():
            raise forms.ValidationError("Password is too common.")

        # NoSymbolValidator
        if not any([sym in symbols for sym in password]):
            raise forms.ValidationError(
                f"Password should contain any of {symbols}")

        return password
