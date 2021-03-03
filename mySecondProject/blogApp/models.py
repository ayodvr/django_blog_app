from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):

    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    featured_image = models.ImageField(upload_to='featured_images',blank=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    published_date = models.DateTimeField(blank=True,null=True)
    # category = models.CharField(max_length=100, default='no_category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def published_post(self):
        self.published_date = timezone.now()
        self.save()
    

class Comment(models.Model):

    post  = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length = 150,default="")
    title = models.CharField(max_length=225)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

# class Category(models.Model):

#     name = models.CharField(max_length = 150)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("post_detail", kwargs={"pk": self.pk}) 
    