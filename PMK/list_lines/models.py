from django.db import models
from core.models import EquipmentBaseModel
from smart_selects.db_fields import ChainedForeignKey

IS_STATUS_CHOICES = [
    (True, 'Да'),
    (False, 'Нет'),
]

# создаем список подразделений
class ListDepartment(models.Model):
    title = models.CharField(max_length=100, verbose_name='Отдел')

    class Meta:
        verbose_name = 'отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.title


# создаем список участков
class ListLine(models.Model):
    title = models.CharField(max_length=100, verbose_name='Участок')
    department_type = models.ForeignKey(ListDepartment,
                                        on_delete=models.CASCADE,
                                        verbose_name='Отдел',
                                        related_name='line')

    class Meta:
        verbose_name = 'участок'
        verbose_name_plural = 'Участки'

    def __str__(self):
        return self.title


# создаем список Системы внутри участков
class SystemLine(models.Model):
    title = models.CharField(max_length=100, verbose_name='Система')
    line_type = models.ForeignKey(ListLine,
                                  on_delete=models.CASCADE,
                                  verbose_name='Участок',
                                  related_name='system')

    class Meta:
        verbose_name = 'системы'
        verbose_name_plural = 'Системы'

    def __str__(self):
        return self.title


# создаем список производителей
class ManufacturerList(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Производитель')

    class Meta:
        verbose_name = 'производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.title
    

# создаем список отделов обслуживания
class MaintenanceList(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Отдел обслуживания')

    class Meta:
        verbose_name = 'отдел обслуживания'
        verbose_name_plural = 'Отделы обслуживания'

    def __str__(self):
        return self.title


# создаем список отделов обслуживания
class EquipmentTypeList(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Тип оборудования')

    class Meta:
        verbose_name = 'тип оборудования'
        verbose_name_plural = 'Типы оборудования'

    def __str__(self):
        return self.title
    

# создаем список отделов обслуживания
class Location(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Расположение')

    class Meta:
        verbose_name = 'расположение'
        verbose_name_plural = 'Расположение'

    def __str__(self):
        return self.title


# создаем список частотных преобразователей внутри участка
class EquipmentList(EquipmentBaseModel):
    title = models.CharField(max_length=100,
                             verbose_name='Оборудование')
    manufacturer = models.ForeignKey(ManufacturerList,
                                     on_delete=models.CASCADE,
                                     verbose_name='Производитель')
    is_status_programm = models.BooleanField(verbose_name='Параметры',
                                             choices=IS_STATUS_CHOICES)
    line_type = models.ForeignKey(ListLine,
                                  on_delete=models.CASCADE,
                                  verbose_name='Участок')
    system_type = ChainedForeignKey(SystemLine,
                                    chained_field="line_type",
                                    chained_model_field="line_type",
                                    show_all=False,
                                    auto_choose=True,
                                    sort=True,
                                    on_delete=models.CASCADE,
                                    verbose_name='Системы',
                                    related_name='system')
    maintenance = models.ForeignKey(MaintenanceList,
                                    on_delete=models.CASCADE,
                                    verbose_name='Отдел обслуживания',
                                    null=False, blank=True)
    equipment_type = models.ForeignKey(EquipmentTypeList,
                                       on_delete=models.CASCADE,
                                       verbose_name='Тип оборудования',
                                       null=False, blank=True,
                                       related_name='equipment')
    location = models.ForeignKey(Location,
                                 on_delete=models.CASCADE,
                                 verbose_name='Расположение',
                                 null=False, blank=True,
                                 related_name='location')

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'

    def __str__(self):
        return f'{self.line_type} — {self.system_type}'
