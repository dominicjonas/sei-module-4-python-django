from django.shortcuts import render
from rest_framework import serializers, viewsets

from .models import Piece
from .serializers import PieceSerializer

# Create your views here.
class PieceViewSet(viewsets.ModelViewSet):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer


