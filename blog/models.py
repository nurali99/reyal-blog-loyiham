from django.db import models
from django.urls import reverse
class Post(models.Model):
    title=models.CharField(max_length=70)
    author=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body=models.TextField()
    time=models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

class Comment(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField()
    text=models.TextField

    def __str__(self):
        return self.name