from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View

from .forms import *

# Create your views here.
class HomeView(View):
    form_class = BudgetForm
    template_name = "panel/form.html"

    def get_context_data(self, **kwargs):
        context = {}
        context['form'] = self.form_class
        return context
        
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
            