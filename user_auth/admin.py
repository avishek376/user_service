from django.contrib import admin
from .models import UserProfile,Role

# Register your models here.

admin.site.register(Role)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    fields = ["user", "phone", "profile_picture","role"]
    list_fields = ["user", "phone","role"]
    filter_fields = ["phone","is_active"]
