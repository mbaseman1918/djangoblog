from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    body = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.user.username + ' ' + self.blogpost.title
