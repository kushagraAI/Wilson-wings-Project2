from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Destination


class UserSerializer(serializers.ModelSerializer):
    destinations = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Destination.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'destinations']


class DestinationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destination
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['id', 'name', 'country', 'description', 'best_time_to_visit',
                  'category', 'image', 'created_at', 'updated_at']
