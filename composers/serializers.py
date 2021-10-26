from rest_framework import serializers
from .models import Composer


class ComposerSerializer(serializers.ModelSerializer):
    class Meta:
        # the model that the serializer is based on
        model = Composer
        # the fields to include in the serialization
        fields = "__all__"
        # Important bit: the depth adds related fields' information into the response
        depth = 1

class ComposerShallowSerializer(serializers.ModelSerializer):
    class Meta:
        # the model that the serializer is based on
        model = Composer
        # the fields to include in the serialization
        fields = "__all__"
        depth = 0
