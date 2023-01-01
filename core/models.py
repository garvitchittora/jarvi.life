from django.db import models

class Site(models.Model):
    site_url = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    favicon = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=100, null=True)
    link_text = models.CharField(max_length=100, null=True)
    copyright = models.CharField(max_length=100, null=True)
    cover_text = models.CharField(max_length=100, null=True)

class Pics(models.Model):
    content = models.JSONField(null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

class BucketList(models.Model):
    content = models.JSONField(null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

class Todo(models.Model):
    content = models.CharField(max_length=100, null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

class FewPoint(models.Model):
    content = models.CharField(max_length=100, null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

class Company(models.Model):
    content = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

class CoverImage(models.Model):
    content = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=100, null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
