from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth import login, authenticate
from django.views import View

from .forms import SignUpForm


def index(request):
    return render(request, 'majesti/home.html')

class CustomLoginView(LoginView):
	template_name = 'majesti/login.html';
	redirect_authenticated_user = True
 	

class HomeView(View):
    template_name = 'majesti/home.html'

    def get(self, request):
        return render(request, self.template_name)
    
class CustomLogoutView(LogoutView):
    template_name = 'majesti/login.html'
    next_page = 'login'
    

class RegisterView(View):
    template_name = 'majesti/register.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        
        return render(request, self.template_name, {'form': form})
    
