# users/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login') # Redirect to login after successful signup
    template_name = 'users/registration/signup.html'

class CustomLoginView(LoginView):
    template_name = 'users/registration/login.html'
    redirect_authenticated_user = True # Redirects logged-in users away from the login page

class ProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'email', 'bio', 'profile_picture', 'phone_number', 'country']
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile') # Redirect back to profile after update

    def get_object(self, queryset=None):
        return self.request.user # Ensure user can only edit their own profile