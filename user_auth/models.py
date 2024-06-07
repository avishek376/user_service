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


class Role(TimeZone):
    role = models.CharField(max_length=10,choices=ROLE_CHOICES,default='staff')

    def __str__(self):
        return self.role


class UserProfile(TimeZone):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    phone = models.CharField(max_length=10,unique=True,null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',blank=True)
    # role = models.CharField(max_length=10,choices=ROLE_CHOICES,default='staff')
    role = models.ManyToManyField(Role,related_name='profile_role')
    is_valid = models.BooleanField(default = False)

    def __str__(self):
        return self.user.username


class Token(TimeZone):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=500, unique=True)
    expires_at = models.DateTimeField()
    revoked = models.BooleanField(default=False)

    def __str__(self):
        return f'Token for {self.user.username}'

