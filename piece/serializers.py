from rest_framework import serializers
from .models import Piece
from composers.serializers import ComposerShallowSerializer

class PieceSerializer(serializers.HyperlinkedModelSerializer):
    # Important bit: overriding the HyperlinkedModelSerializer's default serializer for a related field
    composer = ComposerShallowSerializer(many=True, read_only=True)

    class Meta:
        # the model that the serializer is based on
        model = Piece
        # the fields to include in the serialization
        fields = (
            "id",
            "title",
            # Important bit: these "reverse" relationships weren't included when we had "__all__"
            "composers",
        )
        # Important bit: depth
        depth = 2