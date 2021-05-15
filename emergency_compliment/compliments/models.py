from django.db import models


class Compliment(models.Model):
    text = models.CharField(max_length=600)
