from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class News(models.Model):
    usernews = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='usernews')
    author = models.TextField()
    title=models.TextField()
    description=models.TextField()
    imageurl= models.ImageField(upload_to='news/images', null=True, blank=True)
    publishdate=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title