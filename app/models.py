from django.db import models

class WebNovel(models.Model):
    name = models.CharField(max_length=200)
    cover = models.FileField(upload_to="", default='settings.MEDIA_ROOT/The eternal assassin.jpg')

    def get_absolute_url(self):
        return f"/book/{self.pk}"
