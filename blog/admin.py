from django.contrib import admin
from .models import Post #importing Post from models from the same directory

# Register your models here.
admin.site.register(Post)