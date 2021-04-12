from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView

from .views import index, subject
from .views import TheoryTaskCreateView
from .views import MessageCreateView

urlpatterns = [
    path("message/create/", MessageCreateView.as_view(), name="messagecreate"),
    path("login/", LoginView.as_view(template_name="eduspace/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page='eduspace:login'), name="logout"),
    path("password_change/", PasswordChangeView.as_view(template_name="eduspace/password_change.html"),
         name="password_change"),
    path("password_change/done/", PasswordChangeDoneView.as_view(template_name="eduspace/password_changed.html"),
         name="password_changed"),
    path(
        "password_reset/",
        PasswordResetView.as_view(
            template_name="eduspace/reset_password.html",
            subject_template_name="eduspace/reset_subject.txt",
            email_template_name="eduspace/reset_email.html",
        ),
        name="password_reset"
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="registration/confirm_password.html"
        ),
        name='password_reset_confirm',
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(
            template_name="registration/password_confirmed.html"
        ),
        name="password_reset_complete"
    ),
    path("task/create/", TheoryTaskCreateView.as_view(), name='taskcreate'),
    path('subject/<int:subj_id>', subject, name='subject'),
    path('', index, name='index')
]