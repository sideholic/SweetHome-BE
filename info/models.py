from django.db import models


# Create your models here.
class Info(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()


class News(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    isDelete = models.BooleanField()
