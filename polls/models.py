from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    desc = models.CharField(max_length=2000)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.title
