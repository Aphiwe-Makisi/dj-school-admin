from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.home, name="home"),
    path("student_form/", views.add_new_student, name="student_form"),
]