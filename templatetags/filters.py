from django import template

register = template.Library()

@register.filter(name='myfilter')
def to_string(value):
    return 'valor valor '+value