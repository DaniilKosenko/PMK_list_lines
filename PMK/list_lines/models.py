from django.db import models
from core.models import StatusCPUModel
from smart_selects.db_fields import ChainedForeignKey


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
                                        verbose_name='Отдел')

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
                                  verbose_name='Участок')

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


# создаем список частотных преобразователей внутри участка
class FrequencyConverterList(StatusCPUModel):
    title = models.CharField(max_length=100,
                             verbose_name='Частотный преобразователь')
    manufacturer = models.ForeignKey(ManufacturerList,
                                     on_delete=models.CASCADE)
    is_status_programm = models.BooleanField(verbose_name='Параметры')
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
                                    verbose_name='Системы')

    class Meta:
        verbose_name = 'частотный преобразователь'
        verbose_name_plural = 'Частотные преобразователи'

    def __str__(self):
        return f'{self.line_type} — {self.system_type}'
