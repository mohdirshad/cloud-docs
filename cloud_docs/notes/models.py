from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(max_length=20)
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def __unicode__(self):
        return self.name
        

class Tag(models.Model):
    name = models.CharField(max_length=15)
    
    def __unicode__(self):
        return self.name
        

class Note(models.Model):
    STATUS_CHOICES = (
    ("D", "Draft"),
    ("F", "Final"),
    )
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=50)
    body = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    created_on = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    is_public = models.BooleanField(default=True)
    favorite = models.BooleanField(default=False)
    slug = models.SlugField(max_length=20)
    
    class Meta:
        verbose_name_plural = "Notes"
    
    def __unicode__(self):
        return self.title
        
        

    

