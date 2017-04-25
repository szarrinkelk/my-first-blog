from django.contrib import admin
from .models import Post, Comment

# Register your models here.

admin.site.register(Post) #To make our model visible on the admin page, we need to register the model
admin.site.register(Comment)

