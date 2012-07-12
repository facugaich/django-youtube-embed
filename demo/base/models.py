from django.db import models

class ModelTest(models.Model):
    youtube_id = models.CharField(max_length=11)
