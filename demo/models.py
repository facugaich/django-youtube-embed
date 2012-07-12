from django import models

class ModelTest(models.Model):
    video_id = models.CharField(max_length=11)
