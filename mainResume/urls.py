from django.urls import path

from . import views
app_name="mainResume"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("login_check", views.login_check, name="login_check"),
    path("edit", views.edit, name="edit"),
    path("experience", views.experienceView, name="experience"),
]
