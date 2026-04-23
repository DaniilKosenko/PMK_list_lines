from django import forms

from .models import ListDepartment


# Для использования формы с моделями меняем класс на forms.ModelForm.
class ListDepartmentForm(forms.ModelForm):
    # Все настройки задаём в подклассе Meta.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = ListDepartment
        # Указываем, что надо отобразить все поля.
        fields = '__all__' 