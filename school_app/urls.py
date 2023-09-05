from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.home, name="home"),
    path("student_form/", views.add_new_student, name="student_form"),
    path("sign_in/", views.user_login, name="user_login"),
    path("student_details/<int:pk>", views.view_student_details, name="student_details"),
    path("update_student/<int:pk>", views.update_student_details, name="update_student"),
    path("delete_student/<int:pk>", views.delete_student, name="delete_student"),
]
