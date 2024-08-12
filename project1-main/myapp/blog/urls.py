from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name = 'index'),
    path("details/<str:slug>", views.detail, name = 'details'),
    path("contacts", views.contacts, name = 'contacts'),
    path("about", views.about, name = 'about'),
]