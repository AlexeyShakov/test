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
 
    def __str__(self):
        return '"%s" by %s' % (self.title, self.author)


# class Cat(models.Model):
#     cat_big = models.CharField(max_length=300)
#     cat_small = models.CharField(max_length=300)
#     same_line = models.CharField(max_length=300)
#
#
# class Dog(models.Model):
#     dog_big = models.CharField(max_length=300)
#     dog_small = models.CharField(max_length=300)
#     same_line = models.CharField(max_length=300)
#
#
# class CatDog(models.Model):
#     cat = models.ForeignKey(to=Cat, on_delete=models.CASCADE)
#     dog = models.ForeignKey(to=Dog, on_delete=models.CASCADE)


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.album_name

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)
