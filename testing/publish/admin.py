from django.contrib import admin
from .models import Post, TestSignals

# Register your models here.

admin.site.register(TestSignals)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


