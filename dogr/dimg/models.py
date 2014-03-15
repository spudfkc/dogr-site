from django.db import models

from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField

# Create your models here.
class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField()
    text = models.TextField()
    tags = ListField()
    image = models.TextField()
    comments = ListField(EmbeddedModelField('Comment'))

class Comment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    author = EmbeddedModelField('User')
    text = models.TextField()

class User(models.Model):
    name = models.TextField()
    email = models.EmailField()
