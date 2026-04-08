from django.contrib import admin
from .models import ListDepartment
from .models import ListLine
from .models import SystemLine
from .models import ManufacturerList
from .models import FrequencyConverterList


# Register your models here.
admin.site.register(ListDepartment)
admin.site.register(ListLine)
admin.site.register(ManufacturerList)


class CPUModelAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'manufacturer',
        'is_status_programm',
        'is_status_document',
        'is_status_spare_part',
        'description',
        'line_type',
        'system_type',
    )
    list_editable = (
        'is_status_programm',
        'is_status_document',
        'is_status_spare_part'
    )
    search_fields = ('title',)
    list_filter = ('manufacturer', 'line_type',)
    list_display_links = ('title',)


admin.site.register(FrequencyConverterList, CPUModelAdmin)


class SystemModel(admin.ModelAdmin):
    list_display = (
        'title',
        'line_type',
    )
    list_filter = ('line_type',)


admin.site.register(SystemLine, SystemModel)
