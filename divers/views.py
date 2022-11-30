from django.shortcuts import render
from .functions import multiplicate_by_5
from django.views.generic.edit import CreateView
from . import models
# from django.contrib.auth.forms import UserCreationForm
from . import forms
from django.urls import reverse_lazy

weekdays = [
        'lundi',
        'Tuesday',
        'mercredi',
        'jeudi',
        'vendredi',
        'samedi',
        'dimanche']

# Create your views here.

def home_view(request):
    context = {
        'test' : "Ceci est un test",
        'multi8' : multiplicate_by_5(10),
        'weekdays' : weekdays
    }
    # import pudb;pu.db()
    return render(request, 'divers/home_page.html', context=context)


def about_view(request):
    return render(request, 'divers/about_page.html')

class UserCreateView(CreateView):
    form_class = forms.UserCreationFormCustom
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'