from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustmoUserCreationForm

class SignUpView(CreateView):
    form_class = CustmoUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


