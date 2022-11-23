from django.shortcuts import render
from .functions import multiplicate_by_5

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