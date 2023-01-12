from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=50)
    author = models.ForeignKey('auth.User',
    on_delete=models.CASCADE,
)
    content = models.TextField(max_length=500)
    def __str__(self):
        return self.text[:20]