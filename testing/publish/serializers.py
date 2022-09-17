from rest_framework import serializers
from .models import Post
from .models import Track, Album



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


# class Dog_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Dog
#         fields = '__all__'
#
# class Cat_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cat
#         fields = '__all__'
#
#
# class CatDogSerializer(serializers.ModelSerializer):
#     cat = Cat_Serializer()
#     dog = Dog_Serializer()
#
#     class Meta:
#         model = CatDog
#         fields = ['cat', 'dog']


class TrackSerializer(serializers.ModelSerializer):
    # Без явного обозначения этого поля, патч запрос не будет передавать поле 'id' в JSON
    id = serializers.IntegerField()
    class Meta:
        model = Track
        fields = ['id', 'order', 'title', 'duration']

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album

    # def update(self, instance, validated_data):
    #     # We grab the information of tracks and delete from dict
    #     track_data = validated_data.pop('tracks')
    #     # It's an object
    #     tracks = instance.tracks
    #
    #     instance.album_name = validated_data.get('album_name', instance.album_name)
    #     instance.artist = validated_data.get('artist', instance.artist)
    #     instance.save()
    #
    #     for track in track_data:
    #         Track.objects.filter(id=track.get('id')).update(**track)
    #
    #     return instance

    def update(self, instance, validated_data):
        # We grab the information of tracks and delete from dict
        try:
            track_data = validated_data.pop('tracks')
        except:
            instance.album_name = validated_data.get('album_name', instance.album_name)
            instance.artist = validated_data.get('artist', instance.artist)
            instance.save()
            return instance

        instance.album_name = validated_data.get('album_name', instance.album_name)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.save()
        # Так как у нас может быть много экземпляров в tracks. Если в tracks будет всего один экземпляр, то
        # нужно реализовать по-другому
        for track in track_data:
            id = track.get('id')
            Track.objects.filter(id=id).update(**track)


        return instance