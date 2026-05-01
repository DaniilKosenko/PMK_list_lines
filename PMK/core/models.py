from django.db import models

IS_STATUS_CHOICES = [
    (True, 'Да'),
    (False, 'Нет'),
]

class EquipmentBaseModel(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Логический контроллер')
    is_status_programm = models.BooleanField(default=False,
                                             verbose_name='Программа',
                                             choices=IS_STATUS_CHOICES)
    is_status_document = models.BooleanField(default=False,
                                             verbose_name='Инструкция',
                                             choices=IS_STATUS_CHOICES)
    is_status_spare_part = models.BooleanField(default=False,
                                               verbose_name='ЗИП',
                                               choices=IS_STATUS_CHOICES)
    description = models.TextField(verbose_name='Описание',
                                   null=True,
                                   blank=True)

    class Meta:
        abstract = True

    @property
    def status_text_program(self):
        return 'Да' if self.is_status_programm else 'Нет'
    
    @property
    def status_text_document(self):
        return 'Да' if self.is_status_document else 'Нет'
    
    @property
    def status_text_spare_part(self):
        return 'Да' if self.is_status_spare_part else 'Нет'

