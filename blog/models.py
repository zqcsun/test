from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
class Post(models.Model):
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250, blank=True,null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                             related_name = 'post_user')
    class Meta:
        ordering = ['-id','-created']
        
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(args,kwargs)
    def __str__(self):
        return self.title


# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250, blank=True,null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                             related_name = 'comment_user')
    
    class Meta:
        ordering = ['-id','-created']
        
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(args,kwargs)
    def __str__(self):
        return self.title