from rest_framework import viewsets
from .models import Post, TestSignals
from .serializers import PostSerializer, TestSignalsSerialiser
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import AlbumSerializer
from .models import Album
from django.http import Http404


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


class TestSignalsView(viewsets.ModelViewSet):
    queryset = TestSignals.objects.all()
    serializer_class = TestSignalsSerialiser


