from django import template
from django.utils.html import strip_tags

register = template.Library()


@register.filter(name="reading_time")
def reading_time(text):
    """Return the approximate reading time for a given blog post."""
    num_words = len(strip_tags(text).split())
    avg_speed = 200
    ratio = num_words / avg_speed
    return "< 1 min" if ratio <= 1 else "{} mins".format(int(ratio) + 1)
