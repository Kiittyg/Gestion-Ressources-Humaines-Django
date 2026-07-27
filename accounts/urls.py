from django.urls import path
from .views import login_view,logout_view
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
)

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    
    path(
        "change-password/",
        PasswordChangeView.as_view(
            template_name="accounts/change_password.html"
        ),
        name="change_password",
    ),

    path(
        "change-password/done/",
        PasswordChangeDoneView.as_view(
            template_name="accounts/change_password_done.html"
        ),
        name="password_change_done",
    ),
]