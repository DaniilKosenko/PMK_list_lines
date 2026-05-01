from django.views.generic import ListView, DetailView
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

from .models import (ListDepartment, ListLine,
                     EquipmentList)
from .forms import ListDepartmentForm
from .tables import EquipmentTable
from .filters import EquipmentFilter


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


class FilteredTableEquipment(SingleTableMixin, FilterView):
    table_class = EquipmentTable
    model = EquipmentList
    template_name = 'list_lines/equipment.html'
    filterset_class = EquipmentFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        # Получаем pk из URL
        # Фильтруем по внешнему ключу
        return queryset.filter(system_type=self.kwargs.get('pk'))
