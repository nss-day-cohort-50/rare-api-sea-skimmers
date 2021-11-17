"""View module for handling requests about posts"""
from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth.models import User
from rareapi.models import Author, Post, Category, Comment


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
        # for post in serializer.data:
        #     post['comments'] = Comment.objects.filter(post.id=comment)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """"""
        author = Author.objects.get(user=request.auth.user)
        category = Category.objects.get(pk=request.data["categoryId"])

        post = Post.objects.get(pk=pk)
        post.title = request.data["title"]
        post.publication_date = request.data["publicationDate"]
        post.image_url = request.data["imageUrl"]
        post.content = request.data["content"]
        post.approved = request.data["approved"]
        post.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """"""
        try:
            post = Post.objects.get(pk=pk)
            post.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['get'], detail=False)
    def currentuser(self, request):
        """"""
        author = Author.objects.get(user=request.auth.user)
        try:
            posts = Post.objects.filter(author=author)
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response(
                [], status=status.HTTP_204_NO_CONTENT
            )

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ( 'id', 'content', 'author', 'created_on', )

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

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for games
    Arguments:
        serializer type
    """
    class Meta:
        model = Category
        fields = ('id', 'label')

class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for Posts"""
    author = AuthorSerializer()
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = ('id', 'author', 'category', 'title', 'publication_date', 'image_url', 'content', 'approved')