from django import template
register = template.Library()

@register.filter
def add_module(value, obj):
    return value+obj.__class__.__name__.lower()

@register.filter
def verbose_name(obj):
    return obj._meta.verbose_name


@register.filter
def verbose_name_plural(obj):
    return obj._meta.verbose_name_plural