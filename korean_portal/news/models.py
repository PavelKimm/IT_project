from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='post_pics/test.png', upload_to='post_pics')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        max_size = 800
        if img.height > max_size:
            h_percent = max_size / float(img.size[1])
            w_size = int(float(img.size[0]) * h_percent)
            img.thumbnail((w_size, max_size))
            img.save(self.image.path)
        if img.width > max_size:
            w_percent = max_size / float(img.size[0])
            h_size = int(float(img.size[1]) * w_percent)
            img.thumbnail((max_size, h_size))
            img.save(self.image.path)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.sender}: {self.content}'
