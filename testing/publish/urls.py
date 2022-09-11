from django.contrib import admin
from publish.views import view_post
from django.urls import path

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'^(?P<slug>[a-zA-Z0-9\-]+)', view_post, name='view_post'),
]
