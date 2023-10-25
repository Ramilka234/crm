from rest_framework import serializers
from .models import Houses, House_Photos

class HousesPicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = House_Photos
        fields = ('url',)
class HousesListSerializer(serializers.ModelSerializer):
    house_photos = HousesPicturesSerializer(source='house_photos_set', many=True)
    class Meta:
        model = Houses
        fields = ('name', 'description', 'house_photos')

class HousesDetailSerializer(serializers.ModelSerializer):
    house_photos = HousesPicturesSerializer(source='house_photos_set', many=True)
    class Meta:
        model = Houses
        fields = ('price', 'one_bed','name', 'two_bed', 'description', 'is_prepayment', 'min_prepayment', 'house_photos' )
