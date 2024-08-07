from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='publications/pdfs/%Y/%m/%d/', null=True, blank=True)
    fileName = models.CharField(max_length=255, null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
 


    def __str__(self):
        return self.title