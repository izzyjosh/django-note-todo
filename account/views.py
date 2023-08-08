from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import @ login_required


# function that handle the signup process
def signup(request):
    if request.method == "POST":
        username = request.POST, get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

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
