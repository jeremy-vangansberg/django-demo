from django.views.generic import ListView, DetailView
from .models import *

class FunctionalitiesListView(ListView):
    model = Functionalities
    template_name = 'functionalities/functionalities_list.html'
    context_object_name = 'func_list'

class FunctionalityDetailView(DetailView):
    model = Functionalities
    template_name = 'functionalities/functionality_detail.html'
    context_object_name = 'functionality'