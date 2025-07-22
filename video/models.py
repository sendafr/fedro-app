from django.db import models

# Create your models here.
class Video(models.Model):
    title= models.CharField(max_length=100)
    added= models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='media_cdn/')

    
    def __str__(self):
        return str(self.title)
    
        