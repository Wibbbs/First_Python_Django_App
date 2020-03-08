from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField()
    #thumbnail
    #author

    def __str__(self):
        return self.title

