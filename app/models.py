from django.db import models

class WebNovel(models.Model):
    name = models.CharField(max_length=200)
    cover_path = models.CharField(max_length=200)