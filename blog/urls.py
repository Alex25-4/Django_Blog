from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("more-news/", views.more_news, name="more_news"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
