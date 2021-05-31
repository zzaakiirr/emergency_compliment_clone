from django.db import models
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=240)
    text = RichTextUploadingField()
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        max_length = 100
        if len(self.title) > max_length:
            return f'{self.title[:max_length]}...'
        return self.title
