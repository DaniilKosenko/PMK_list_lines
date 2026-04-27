from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .models import ListDepartment, ListLine
from .forms import ListDepartmentForm


class ListDepartment(ListView):
    template_name = 'list_lines/index.html'
    model = ListDepartment
    context_object_name = 'department_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ListDepartmentForm()  # Добавляем форму в контекст
        return context


class Lines(DetailView):
    template_name = 'list_lines/lines.html'
    model = ListLine
    context_object_name = 'line'


def equipment(request):
    template = 'list_lines/equipment.html'
    return render(request, template)
