from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length = 64)
    description = models.CharField(max_length = 256)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length = 64)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length = 64)
    preparation_steps = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    preparation_steps = models.BooleanField(default = False)
    updated_at = models.DateTimeField(auto_now = True)
    is_published = models.BooleanField(default = False)
    cover = models.ImageField(upload_to = 'recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True)
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
