from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
	template_name = 'accounts/login.html';
	redirect_authenticated_user = True
 	

class HomeView(View):
    template_name = 'majesti/home.html'

    def get(self, request):
        return render(request, self.template_name)
    
class CustomLogoutView(LogoutView):
    template_name = 'accounts/login.html'
    next_page = 'login'