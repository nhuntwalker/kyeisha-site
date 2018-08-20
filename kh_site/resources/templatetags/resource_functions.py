from django import template
from django.utils.html import strip_tags
import re

register = template.Library()


@register.filter(name="format_phone")
def format_phone(text):
    """Return the approximate reading time for a given blog post."""
    phone_number = strip_tags(text)
    if phone_number[0] != "1":
        phone_number = "1" + phone_number
    number_parts = re.findall(r'\d+', phone_number)
    output = "+" + "".join(number_parts)
    return output
