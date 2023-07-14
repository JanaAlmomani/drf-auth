from rest_framework import serializers
from .models import Snack ,Post

class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Snack
        fields = ('id', 'purchaser', 'title','description','created_at','updated_at')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields = ('title', 'desc')