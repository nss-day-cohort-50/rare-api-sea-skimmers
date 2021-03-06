from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth.models import User
from rareapi.models import  Comment, Author, Post


class CommentView(ViewSet):

    def create(self, request):

        author = Author.objects.get(user=request.auth.user)
        post = Post.objects.get(id=request.data['postId'])

        try:
            comment = Comment.objects.create(
                post = post,
                author = author,
                content = request.data["content"],
            )
            serializer = CommentSerializer(comment, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):

        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        author = Author.objects.get(user=request.auth.user)
        post = Post.objects.get(id=request.data['postId'])

        # Do mostly the same thing as POST, but instead of
        # creating a new instance of Game, get the game record
        # from the database whose primary key is `pk`
        comment = Comment.objects.get(pk=pk)
        comment.content = request.data["content"]
        comment.post = post
        comment.author = author
        comment.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({'yeah yeah yeah'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Comment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CommentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Comment
        fields = ( 'id', 'content', 'author', 'created_on', )