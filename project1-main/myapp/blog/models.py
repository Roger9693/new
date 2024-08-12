from django.db import models
from django.utils.text import slugify

class Categorys(models.Model):
    name = models.CharField(max_length=100)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    img_url = models.URLField(null=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Categorys,  on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class About(models.Model):
    content = models.TextField()