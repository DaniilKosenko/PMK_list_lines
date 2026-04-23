from django.urls import path

from .views import index, lines, equipment

app_name = 'list_lines'

urlpatterns = [
    path('', index, name='index'),
    path('lines', lines, name='lines'),
    path('equipment', equipment, name='equipment'),
 ]
