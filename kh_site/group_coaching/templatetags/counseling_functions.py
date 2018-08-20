from django import template

register = template.Library()


@register.filter(name="format_location")
def format_location(text):
    """Replace all the spaces with plus signs."""
    return text.replace(' ', '+')

@register.filter(name="lump_discount")
def lump_discount(text, sessions=8):
    """Take the price of one event and multiply by the number of sessions - 1."""
    total = float(text) * (int(sessions) - 1)
    return "{total:.2f}".format(total=total)