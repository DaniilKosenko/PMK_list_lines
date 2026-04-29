from django_tables2 import Table
from .models import FrequencyConverterList


class EquipmentTable(Table):

    class Meta:
        model = FrequencyConverterList
        fields = ('title', 'manufacturer', 'is_status_programm',
                  'is_status_document')
        
