from django.urls import path

from . import views

app_name = 'sekolah'
urlpatterns = [
    path("", views.index, name='index'),
    path("create/", views.create, name='create'),
    path("", views.create_view),
]