from django.db import models

class Note(models.Model):
    message = models.CharField(max_length=200)
