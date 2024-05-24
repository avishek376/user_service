from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TimeZone(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


ROLE_CHOICES = [
    ('staff','staff'),
    ('manager','manager'),
]


class UserProfile(TimeZone):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10,unique=True,null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',blank=True)
    role = models.CharField(max_length=10,choices=ROLE_CHOICES,default='staff')
    is_valid = models.BooleanField(default = False)