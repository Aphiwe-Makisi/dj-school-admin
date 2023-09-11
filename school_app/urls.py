from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("student_list/", views.get_all_students, name="student_list"),
    path("student_form/", views.add_new_student, name="student_form"),
    path("login/", auth_view.LoginView.as_view(template_name="school_app/user_login_form.html"), name="login"),
    path("logout/", auth_view.LogoutView.as_view(template_name="school_app/user_login_form.html"), name="logout"),
    path("student_details/<int:pk>", views.view_student_details, name="student_details"),
    path("update_student/<int:pk>", views.update_student_details, name="update_student"),
    path("delete_student/<int:pk>", views.delete_student, name="delete_student"),
    path("user_registration/", views.user_registration, name="user_registration")
]
