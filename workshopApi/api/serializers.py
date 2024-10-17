import base64
import hashlib
import random
import string

from rest_framework import serializers

from workshopApi.models import *


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = "__all__"
        depth = 1


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"
        depth = 1


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = "__all__"
        depth = 1


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "UUID", "username", "email"]


def base64_encode(data):
    return base64.b64encode(data.encode("utf-8")).decode("utf-8")


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ["name"]

    def create(self, validated_data):
        validated_data["adminKey"] = base64_encode(
            "".join(random.choices(string.ascii_lowercase, k=50))
        )
        platform = Platform.objects.create(**validated_data)
        return platform


class ClientSerializer(serializers.ModelSerializer):
    apiKey = serializers.CharField(write_only=True, required=False)
    adminKey = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Client
        fields = ("email", "nbOfAvailableRequests", "apiKey", "adminKey")

    def create(self, validated_data):
        admin_key = validated_data.pop("adminKey", None)

        try:
            platform = Platform.objects.get(adminKey=base64_encode(admin_key))
        except Platform.DoesNotExist:
            raise serializers.ValidationError("Invalid adminKey. Platform not found.")

        validated_data["platform"] = platform
        apiKey = "".join(random.choices(string.ascii_lowercase, k=50)).encode("utf-8")
        hash_object = hashlib.sha256(apiKey)
        validated_data["apiKey"] = hash_object.hexdigest()

        client = Client.objects.create(**validated_data)

        client.raw_api_key = apiKey.decode("utf-8")

        return client

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if hasattr(instance, "raw_api_key"):
            representation["apiKey"] = instance.raw_api_key

        return representation
