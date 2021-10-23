from rest_framework import serializers
from .models import Composer


class ComposerSerializer(serializers.ModelSerializer):
    class Meta:
        # the model that the serializer is based on
        model = Composer
        # the fields to include in the serialization
        fields = "__all__"