from django import template
from health.models import Social


register = template.Library()


@register.simple_tag()
def get_social_links():
    return Social.objects.all()