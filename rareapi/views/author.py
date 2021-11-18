from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers

from rareapi.models import  Comment, Author, Post



class AuthorView(ViewSet):


    @action(methods=['get'], detail=False)
    def currentuser(self, request):
        """"""
        author = Author.objects.get(user=request.auth.user)
        try:
            serializer = AuthorSerializer(author, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response(
                [], status=status.HTTP_204_NO_CONTENT
            )

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users on authors on posts"""
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'is_staff', )

class AuthorSerializer(serializers.ModelSerializer):
    """JSON serializer for authors on posts"""
    user = UserSerializer()
    class Meta:
        model = Author
        fields = ('id', 'user', 'bio', )