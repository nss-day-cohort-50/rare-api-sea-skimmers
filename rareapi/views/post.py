"""View module for handling requests about posts"""
from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth.models import User
from rareapi.models import Author, Post, Category


class PostView(ViewSet):
    """Rare Posts"""

    def create(self, request):
        """Handle Post operations
        Returns:
            Response -- JSON serialized post instance
        """

        author = Author.objects.get(user=request.auth.user)
        category = Category.objects.get(pk=request.data["categoryId"])

        try:
            post = Post.objects.create(
                author = author,
                category = category,
                title = request.data["title"],
                publication_date = request.data["publicationDate"],
                image_url = request.data["imageUrl"],
                content = request.data["content"],
                approved = request.data["approved"]
            )
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """"""
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """"""
        posts = Post.objects.all()

        serializer = PostSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users on authors on posts"""
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username')

class AuthorSerializer(serializers.ModelSerializer):
    """JSON serializer for authors on posts"""
    user = UserSerializer()
    class Meta:
        model = Author
        fields = ('id', 'user', 'bio')

class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for Posts"""
    author = AuthorSerializer()
    class Meta:
        model = Post
        fields = ('id', 'author', 'category', 'title', 'publication_date', 'image_url', 'content', 'approved')