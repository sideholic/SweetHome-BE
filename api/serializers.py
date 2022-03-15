from rest_framework import serializers


class nearby_serializer(serializers.Serializer):
    x = serializers.CharField(required=False)
    y = serializers.CharField(required=False)


class detail_serializer(serializers.Serializer):
    subject = serializers.CharField(default='apt')
