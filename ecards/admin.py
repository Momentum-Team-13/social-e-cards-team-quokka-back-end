from django.contrib import admin
from .models import FollowRequest, User, Card
# Register your models here.

admin.site.register(User)
admin.site.register(Card)
admin.site.register(FollowRequest)
