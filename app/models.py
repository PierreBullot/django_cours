from django.db import models
from. import settings

class WebNovel(models.Model):
    name = models.CharField(max_length=200)
    cover = models.FileField(upload_to=settings.MEDIA_ROOT, default='settings.MEDIA_ROOT/The eternal assassin.jpg')
