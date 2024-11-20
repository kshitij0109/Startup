from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    Name = models.CharField(max_length=50)
    startupName = models.CharField(max_length=60)
    description = models.TextField()
    image1 = models.ImageField(upload_to='photos/image1/',null=True, blank=True)
    image2 = models.ImageField(upload_to='photos/image2/',null=True, blank=True)
    image3 = models.ImageField(upload_to='photos/image3/',null=True, blank=True)
    revenue = models.BigIntegerField(default=0)
    date = models.DateTimeField(null=True)
    location = models.CharField(max_length=100, null=True)
    contact_No = models.CharField(max_length=10, null=True)


    def __str__(self):
        return f'{self.user.username} - {self.startupName[:20]}'



class Tweet(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tweet_images', blank=True, null=True)