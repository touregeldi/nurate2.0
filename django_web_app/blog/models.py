from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os

class Post(models.Model):
	title = models.CharField(max_length=100)
	file = models.FileField(null=True,blank=True,upload_to='Files')
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def extension(self):
		name, extension = os.path.splitext(self.file.name)
		return extension

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

        

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)