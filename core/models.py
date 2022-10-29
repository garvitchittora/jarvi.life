from django.db import models

class Pics(models.Model):
    content = models.JSONField(null=True)