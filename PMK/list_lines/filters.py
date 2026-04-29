import django_filters
from .models import FrequencyConverterList

class EquipmentFilter(django_filters.FilterSet):
    class Meta:
        model = FrequencyConverterList
        fields = {'title': ['icontains'], 'manufacturer': ['exact'],
                  'is_status_programm': ['exact']}
