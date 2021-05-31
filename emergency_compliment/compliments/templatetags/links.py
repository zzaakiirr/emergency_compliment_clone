from django import template

from compliments.models import Link


register = template.Library()

@register.simple_tag
def telegram_url(escape='#'):
    link = Link.objects.filter(social_media=Link.SocialMedia.TELEGRAM).first()
    return link.url if link is not None else escape


@register.simple_tag
def instagram_url(escape='#'):
    link = Link.objects.filter(social_media=Link.SocialMedia.INSTAGRAM).first()
    return link.url if link is not None else escape
