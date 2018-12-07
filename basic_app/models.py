from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Subcategory(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=100)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    body = models.TextField()

    def __str__(self):
        return self.title
