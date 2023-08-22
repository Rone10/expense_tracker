from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm, UserCreateForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomLoginForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('expenses:expenses')

class UserSignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('users:login')
    
    def fom_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(UserSignUpView, self).form_valid(form)
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('expenses:expenses')
        return super(UserSignUpView, self).get(request, *args, **kwargs)