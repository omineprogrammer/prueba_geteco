from django import template


register = template.Library()


@register.filter
def get_attr(obj, attr):
    return getattr(obj, attr, None)


@register.simple_tag
def define(val=None): return val


@register.filter
def fields_name_from_list(obj_list):
    if obj_list:
        return [f.name for f in obj_list[0]._meta.fields]
    else:
        return []


@register.filter
def get_fields(obj):
    fields = [f.name for f in obj._meta.fields]
    return {f: getattr(obj, f, None) for f in fields}
