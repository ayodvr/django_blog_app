from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Complete(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    address = models.TextField()
    avatar = models.ImageField(upload_to='featured_images',blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})
