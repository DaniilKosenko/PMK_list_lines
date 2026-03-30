from django.db import models


# создаем список подразделений
class ListВepartment(models.Model):
    title = models.CharField(max_length=100)

