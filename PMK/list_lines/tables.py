from django_tables2 import Table, Column
from .models import EquipmentList


class EquipmentTable(Table):
    title = Column(verbose_name='Название')
    is_status_programm = Column(
        verbose_name='Статус программы',
        attrs={'td': {'class': lambda record: 'table-success'
                      if record.is_status_programm else 'table-danger'}}
    )
    is_status_document = Column(
        verbose_name='Документация',
        attrs={'td': {'class': lambda record: 'table-success'
                      if record.is_status_document else 'table-danger'}}
    )
    is_status_spare_part = Column(
        verbose_name='ЗИП',
        attrs={'td': {'class': lambda record: 'table-success'
                      if record.is_status_spare_part else 'table-danger'}}
    )

    def render_title(self, record):
        return f'{record.title}'

    def render_is_status_programm(self, record):
        return 'да' if record.is_status_programm else 'нет'
    
    def render_is_status_document(self, record):
        return 'да' if record.is_status_document else 'нет'
    
    def render_is_status_spare_part(self, record):
        return 'да' if record.is_status_spare_part else 'нет'
      
    class Meta:
        model = EquipmentList
        fields = ('equipment_type',
                  'title',
                  'manufacturer',
                  'is_status_programm',
                  'is_status_document',
                  'is_status_spare_part')
        
