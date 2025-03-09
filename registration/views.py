from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

# Create your views here.
class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    success_url = reverse_lazy('index')

    def form_valid(self, form):
       login(self.request, form.save())
       return super().form_valid(form)