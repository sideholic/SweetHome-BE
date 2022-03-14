from rest_framework import serializers


class NearbySerializer(serializers.Serializer):
    x = serializers.CharField(max_length=100),
    y = serializers.CharField(max_length=100)
