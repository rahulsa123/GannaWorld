from django.urls import path, reverse_lazy

from . import views
from django.contrib.auth import views as auth_view
app_name = "user"
urlpatterns = [
    path("register/", views.register, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path("login/", auth_view.LoginView.as_view(template_name="user/login.html"),
         name="login"),
    path("logout/",
         auth_view.LogoutView.as_view(template_name="user/logout.html"),
         name="logout"),

    path(
        "password_change/",
        auth_view.PasswordChangeView.as_view(
            template_name="user/password_change_form.html",
            success_url=reverse_lazy("user:password_change_done")
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_view.PasswordChangeDoneView.as_view(
            template_name="user/password_change_done.html"
        ),
        name="password_change_done",
    ),
    # reset password urls
    path(
        "password_reset/",
        auth_view.PasswordResetView.as_view(
            template_name="user/password_reset_form.html",
            success_url=reverse_lazy("user:password_reset_done"),
            email_template_name="user/password_reset_email.html"
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_view.PasswordResetDoneView.as_view(
            template_name="user/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_view.PasswordResetConfirmView.as_view(
            template_name="user/password_reset_confirm.html",
            success_url=reverse_lazy("user:password_reset_complete")
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_view.PasswordResetCompleteView.as_view(
            template_name="user/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),

]
