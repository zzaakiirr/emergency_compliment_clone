import random

from django.db import models
from django.utils.translation import gettext_lazy as _

from .helpers import truncate_text


class Compliment(models.Model):
    text = models.CharField(max_length=600, null=False, blank=False)

    @classmethod
    def get_random(cls):
        max_id = cls.objects.all().aggregate(max_id=models.Max("id")).get('max_id')

        if not max_id:
            return

        instance = None
        while not instance:
            pk = random.randint(1, max_id)
            instance = cls.objects.filter(pk=pk).first()

        return instance

    def __str__(self):
        return truncate_text(self.text)


class Link(models.Model):

    class SocialMedia(models.TextChoices):
        TELEGRAM = 'TG', _('Telegram')
        INSTAGRAM = 'IN', _('Instagram')

    social_media = models.CharField(
        max_length=2,
        choices=SocialMedia.choices,
        default=SocialMedia.TELEGRAM
    )
    url = models.URLField(null=False, blank=False)

    def __str__(self):
        return truncate_text(f'{self.social_media} - {self.url}')

    def save(self, *args, **kwargs):
        if not self.pk and Link.objects.count() == 2:
            return
        return super(Link, self).save(*args, **kwargs)
