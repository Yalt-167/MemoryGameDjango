from django.contrib import admin

from .models import UserProfile, UserHistory,Score


# Register your models here. -> allow us to access it from the admin panel

admin.site.register(UserProfile)
admin.site.register(UserHistory)
admin.site.register(Score)


