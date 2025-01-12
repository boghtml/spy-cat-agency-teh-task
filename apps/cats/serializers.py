# apps/cats/serializers.py

import requests
from rest_framework import serializers
from .models import Cat

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__' 

    def validate_breed(self, value):

        CAT_BREEDS_URL = "https://api.thecatapi.com/v1/breeds"

        try:
            response = requests.get(CAT_BREEDS_URL, timeout=5)
            response.raise_for_status()
        except requests.RequestException:
            raise serializers.ValidationError("There was an error connecting to TheCatAPI. Please try again later.")

        breeds_data = response.json() 
       
        valid_breed_names = [breed['name'] for breed in breeds_data]

        if value not in valid_breed_names:
            raise serializers.ValidationError(f"Breed '{value}' not found in TheCatAPI.")
        return value
