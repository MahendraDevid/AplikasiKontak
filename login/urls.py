from django.urls import path

# import class View
from .views import CustomLoginView, HomeView, CustomLogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    
    path('logout/', CustomLogoutView.as_view(), name='logout')
]