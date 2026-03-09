from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=200,null=True)
    content = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title