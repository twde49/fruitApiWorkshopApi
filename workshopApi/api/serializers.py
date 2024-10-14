from workshopApi.models import Color,Fruit,Season,CustomUser
from rest_framework import serializers


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = '__all__'
        depth = 1

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
        depth = 1

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'
        depth = 1


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','UUID','username','email']
