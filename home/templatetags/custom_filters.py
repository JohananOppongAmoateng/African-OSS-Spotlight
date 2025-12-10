# Custom template filters for African OSS Spotlight

from django import template

register = template.Library()

@register.filter(name='split')
def split(value, delimiter=','):
    """Split a string by delimiter"""
    if value:
        return [item.strip() for item in value.split(delimiter)]
    return []
