from django.urls import path

from .views import index, subject
from .views import TheoryTaskCreateView

urlpatterns = [
    path("task/create/", TheoryTaskCreateView.as_view(), name='taskcreate'),
    path('subject/<int:subj_id>', subject, name='subject'),
    path('', index, name='index')
]