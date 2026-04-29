from django.urls import path

from .views import ListDepartment, Lines, FilteredTableEquipment

app_name = 'list_lines'

urlpatterns = [
    path('', ListDepartment.as_view(), name='index'),
    path('lines/<int:pk>', Lines.as_view(), name='lines'),
    path('equipment/<int:pk>', FilteredTableEquipment.as_view(),
         name='equipment'),
 ]
