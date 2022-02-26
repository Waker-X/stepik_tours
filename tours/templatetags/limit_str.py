from django import template

register = template.Library()


@register.filter
def limit_str(in_text, limit):
    x = in_text.split()
    y = x[:int(limit)]
    result = f"{' '.join(y)} ..."
    return result
