# templatetags/max_filter.py
from django import template

register = template.Library()


@register.filter
def max_filter(value, arg):
    return max(value, arg)
