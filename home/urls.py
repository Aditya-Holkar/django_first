from django.urls import path

from home import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]