from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DetailView,DeleteView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, UpdateForm,NewForm
from django.contrib.auth.models import User
from .models import Complete

# Create your views here.

class UserCreateView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserNewForm(CreateView):
    form_class = NewForm
    template_name = 'registration/complete_profile.html'
    # success_url = reverse_lazy('login')

class UserUpdateView(UpdateView):
    model = User
    form_class = UpdateForm
    template_name = 'registration/user_update.html'
    success_url = reverse_lazy('user_detail')


class UserDetailView(DetailView):
    model = User
    context_object_name = 'user_detail'
    template_name = "registration/profile.html"

class UserUpdateProfile(UpdateView):
    model = Complete
    form_class = NewForm
    template_name = 'registration/complete_profile.html'

class UserDeleteView(DeleteView):
    model = User
    template_name = 'registration/delete_profile.html'
    success_url = '/'
