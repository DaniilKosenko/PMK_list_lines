import django_filters
from .models import EquipmentList


class EquipmentFilter(django_filters.FilterSet):
    class Meta:
        model = EquipmentList
        fields = {'equipment_type': ['exact']}
