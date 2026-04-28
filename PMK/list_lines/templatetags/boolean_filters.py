from django import template

register = template.Library()

@register.filter
def bool_to_text(value):
    return 'Да' if value else 'Нет'
