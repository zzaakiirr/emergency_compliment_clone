import random

from django.db import models


class Compliment(models.Model):
    text = models.CharField(max_length=600)

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
        max_length = 100
        if len(self.text) > max_length:
            return f'{self.text[:max_length]}...'
        return self.text
