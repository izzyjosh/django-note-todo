from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import update_session_auth_hash


# function that handle the signup process
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("password1")

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if password == confirm_password:
                    User.objects.create_user(
                        username=username,
                        email=email,
                        password=password
                    )
                    messages.info(request, "successfully created account")
                    return redirect("signin")
                else:
                    messages.error(request, "both password do not correspond ")
            else:
                messages.error(request, "email already exist")
        else:
            messages.error(request, "the username already exist")
    return render(request, "signup.html")


# function that handles the signin
def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("#")
        else:
            messages.error(request, "invalid email or password")
    return render(request, "signin.html")


# function that logs out user
@login_required
def logout(request):
    auth.logout(request)
    return redirect("signin")


def setpassword(request, uidb64, token):
    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.get(email=email)
        username = user.username
        user_password = user.password
        log = auth.authenticate(username=username, password=user_password)
        if log is not None:
            auth.login(request, log)
        form = MySetPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.info(request, "successfully reset password")
            return redirect("password_reset_complete")
        else:
            messages.error(request, "the form contains invalid data")
    else:
        form = MyPasswordResetForm()
    return render(request, "password_reset_confirm.html", {"form": form})
