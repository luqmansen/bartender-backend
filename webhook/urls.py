from django.urls import path

from webhook import views

urlpatterns = [
    path("update_server/", views.update, name="update"),
]
