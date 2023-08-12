from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import forms

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.logout, name="logout"),
    path('password-reset/', PasswordResetView.as_view(
        template_name="reset_password.html"), name="password-reset"),

    path("password-reset/done", PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",
         views.MySetPasswordForm, name="password_reset_confirm"),
    path("password-reset-complete/", PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"), name="password_reset_confirm"),
]
