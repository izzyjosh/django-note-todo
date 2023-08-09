from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import *

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.logout, name="logout"),
    path("resetpassword/", PasswordResetView.as_view(
        template_name="reset_password.html",
        form_class=MyPasswordResetForm), name="reset_password"
    ),
    path("passwordreset/done/", PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"), name="password_reset_done"
    ),
    path("passwordreset/confirm/", views.setpassword,
         name="password_reset_confirm"
         ),
    path("passwordreset/complete", PasswordResetCompleteView.as_view(
        template_name="password_reset_complete,html"
    ), name="password_reset_complete")
]
