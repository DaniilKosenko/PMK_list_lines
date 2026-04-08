from django.db import models


class StatusCPUModel(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Логический контроллер')
    is_status_programm = models.BooleanField(default=False,
                                             verbose_name='Программа')
    is_status_document = models.BooleanField(default=False,
                                             verbose_name='Инструкция')
    is_status_spare_part = models.BooleanField(default=False,
                                               verbose_name='ЗИП')
    description = models.TextField(verbose_name='Описание',
                                   null=True,
                                   blank=True)

    class Meta:
        abstract = True
