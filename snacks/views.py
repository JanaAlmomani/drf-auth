from django.shortcuts import render
from rest_framework import generics
from .models import Snack ,Post
from .serializers import SnackSerializer,PostSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly



# Create your views here.

# ListAPIView
class SnacksList(generics.ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = [IsAuthenticated]

# RetrieveAPIView RetrieveUpdateAPIView
class SnackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = [IsOwnerOrReadOnly]


class PostsList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]