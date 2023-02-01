from django.urls import path


from . import views

app_name = 'perusahaan'
urlpatterns = [
    path("", views.list, name='list'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path("update/<int:id>/", views.update, name='update'),



    path("create/", views.create, name='create'),
    #path("", views.create_view),
]