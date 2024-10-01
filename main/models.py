from django.db import models
from django.utils.text import slugify


class Direction(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    sort_order = models.IntegerField()
    
    def __str__(self):
        return self.title
        
        
class Doctors(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    directions = models.ManyToManyField(Direction)
    description = models.TextField()
    birth_date = models.DateField()
    experience = models.IntegerField()
    sort_order = models.IntegerField()
    
    def __str__(self):
        return self.name
    