from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


# https://code.tutsplus.com/ru/tutorials/using-celery-with-django-for-background-task-processing--cms-28732
class Post(models.Model):
    # get_user_model gets the currents user. So if a user has signed in we can get him/her by using get_user_model()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField('Created Date', default=timezone.now)
    title = models.CharField('Title', max_length=200)
    content = models.TextField('Content')
    slug = models.SlugField('Slug')
 
    def __str__(self):
        return '"%s" by %s' % (self.title, self.author)
