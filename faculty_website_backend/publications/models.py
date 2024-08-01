from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    description = models.TextField()
    fileData = models.TextField() 
    fileName = models.CharField(max_length=255)

    def __str__(self):
        return self.title