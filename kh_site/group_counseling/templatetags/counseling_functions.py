from django import template

register = template.Library()


@register.filter(name="format_location")
def format_location(text):
    """Replace all the spaces with plus signs."""
    return text.replace(' ', '+')
