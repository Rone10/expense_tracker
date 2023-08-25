from django import template

register = template.Library()


@register.filter
def min_filter(value, arg):
    return min(value, arg)
