from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomLoginForm, UserCreateForm

# Create your views here.


class UserLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = CustomLoginForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("expenses:expenses")


class UserSignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("users:login")

    def fom_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(UserSignUpView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("expenses:expenses")
        return super(UserSignUpView, self).get(request, *args, **kwargs)
