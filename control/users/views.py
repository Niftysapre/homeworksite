from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin



def users(request):
    return HttpResponse('users')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('main')
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

class registerUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_content = {'title': 'Регистрация'}

    def get_success_url(self):
        return reverse_lazy('login')

def profile(request):
    return render(request, 'users/profile.html')

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_content = {'title': 'Profile'}

    def get_success_url(self):
        return reverse_lazy('profile')
    def get_object(self, queryset=None):
        return self.request.user