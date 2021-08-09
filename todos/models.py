from django.db import models

class Todo(models.Model):
    foto = models.CharField(max_length=1000)
    author = models.CharField(max_length=200,blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    body = models.TextField()
    
    def __str__(self):
        return self.title