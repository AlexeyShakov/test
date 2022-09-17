from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_multiple_model.views import FlatMultipleModelAPIView, ObjectMultipleModelAPIView
from .serializers import AlbumSerializer
from .models import Album


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class Dog_cat_view_api(ObjectMultipleModelAPIView):
#     def get_querylist(self):
#
#         #this is a user(header Authorization:token 123123)
#         user = self.request.user
#         #this is data (in body(form-data))
#         data = self.request.data
#
#         querylist = [
#             {'queryset': Dog.objects.all(), 'serializer_class': Dog_Serializer},
#             {'queryset': Cat.objects.all(), 'serializer_class': Cat_Serializer},
#         ]
#         return querylist


# class CatDogView(viewsets.ModelViewSet):
#     queryset = CatDog.objects.all()
#     serializer_class = CatDogSerializer


class AlbumView(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

