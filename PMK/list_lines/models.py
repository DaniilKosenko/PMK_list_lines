from django.db import models


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
                                        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'учсток'
        verbose_name_plural = 'Участки'

    def __str__(self):
        return self.title
