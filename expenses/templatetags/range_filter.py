from django import template

register = template.Library()


@register.filter
def range_filter(value, end_value):
    return range(value, end_value)
