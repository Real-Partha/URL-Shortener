from django.db import models

# Create your models here.
class Url(models.Model):
    original_link = models.URLField(max_length=1000)
    shortened_link = models.CharField(max_length=15)
    time_created = models.DateTimeField(auto_now_add=True)
    access_count = models.IntegerField(default=0)

    def __str__(self):
        return self.original_link