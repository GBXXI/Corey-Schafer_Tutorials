from django.contrib import admin

# Register your models here. In order to be shown in the admin page.
from blog.models import Post
admin.site.register(Post)
