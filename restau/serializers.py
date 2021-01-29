import base64
import os
from django.conf import settings
from rest_framework import serializers
from restau import models


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Restaurant
        fields = ["id","name","direction","phone"]



class RecipeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        restaurant = models.Restaurant.objects.get(pk=validated_data['restaurant_id'])
        validated_data["restaurant"] = restaurant
        recipe = models.Recipe.objects.create(**validated_data)
        return recipe

    class Meta:
        model = models.Recipe
        fields = ["id","name","type","ingredient"]