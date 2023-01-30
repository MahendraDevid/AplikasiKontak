from django.urls import path
from django.contrib import admin

from . import views

app_name = 'sekolah'
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.list, name='list'),
    path("", views.Sekolah, name='sekolah'),
    path('delete/<int:id>', views.delete, name='delete'),
    path("update/<int:id>", views.update, name='update'),



    path("create/", views.create, name='create'),
    #path("", views.create_view),
]