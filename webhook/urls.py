from django.urls import path

from webhook import views

urlpatterns = [
    path("git_deploy/", views.update, name="update"),
    path("healthz/", views.healtz, name="health"),
]
