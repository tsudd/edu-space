from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView
from knox import views as knox_views
# from .views import index, subject, task, message_del
# from .views import MessageCreateView, TaskCreateView
from .api import AccountViewSet, LoginAPI, AccountAPI, SubjectList, SubjectDetail, TaskList, TaskDetail


app_name = 'eduspace'

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/account', AccountAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/subjects', SubjectList.as_view(), name="subjects"),
    path('api/subjects/<int:pk>', SubjectDetail.as_view(), name="subject-detail"),
    path('api/tasks', TaskList.as_view(), name="tasks"),
    path('api/tasks/<int:pk>', TaskDetail.as_view(), name="task-detail"),
    # path('api/subjects/<int:subject_id>',
    #      SubjectDetail.as_view(), name="subject-detail"),
    # path('api/auth/teacher/<int:teacher_id>'),
    # path('api/subjects', SubjectsAPI.as_view(), name="subjects"),
    # path('', include(router.urls)),
    # path('task/<int:task_id>', task, name='task'),
    # path("message/create/", MessageCreateView.as_view(), name="messagecreate"),
    # path("login/", LoginView.as_view(template_name="eduspace/registration/login.html"), name="login"),
    # path("logout/", LogoutView.as_view(next_page='eduspace:login'), name="logout"),
    # path("password_change/", PasswordChangeView.as_view(template_name="eduspace/registration/password_change.html"),
    #      name="password_change"),
    # path("password_change/done/", PasswordChangeDoneView.as_view(
    #     template_name="eduspace/registration/password_changed.html"),
    #     name="password_changed"),
    # path(
    #     "password_reset/",
    #     PasswordResetView.as_view(
    #         template_name="eduspace/registration/reset_password.html",
    #         subject_template_name="eduspace/registration/reset_subject.txt",
    #         email_template_name="eduspace/registration/reset_email.html",
    #     ),
    #     name="password_reset"
    # ),
    # path(
    #     "reset/<uidb64>/<token>/",
    #     PasswordResetConfirmView.as_view(
    #         template_name="registration/confirm_password.html"
    #     ),
    #     name='password_reset_confirm',
    # ),
    # path(
    #     "reset/done/",
    #     PasswordResetCompleteView.as_view(
    #         template_name="registration/password_confirmed.html"
    #     ),
    #     name="password_reset_complete"
    # ),
    # path("practicetask/create/", TaskCreateView.as_view(), name='taskcreate'),
    # path('subject/<int:subj_id>', subject, name='subject'),
    # path('', index, name='index'),
    # path('message/del/<int:mes_id>', message_del, name="mes_del")
]
