from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # This field automatically adds slug to "slug" field
    prepopulated_fields = {'slug': ('title',)}


