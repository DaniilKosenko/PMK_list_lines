from django.shortcuts import render

from .models import ListDepartment
from .forms import ListDepartmentForm


def index(request):
    department_list = ListDepartment.objects.select_related()
    form = ListDepartmentForm
    context = ({'department_list': department_list, 'form': form})
    return render(request, 'list_lines/index.html', context)


def lines(request):
    template = 'list_lines/lines.html'
    return render(request, template)


def equipment(request):
    template = 'list_lines/equipment.html'
    return render(request, template)
