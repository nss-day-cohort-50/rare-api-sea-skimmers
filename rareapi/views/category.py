from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rareapi.models.category import Category

class CategoryView(ViewSet):
    """ Rare Categories """
    
    def create(self, request):
        """Handle Category operations
        
        Returns:
            Response -- JSON serialized category instance"""
            
        try:
            category = Category.objects.create(
                label=request.data["label"]
            )
            serializer = CategorySerializer(category, context={'request': request})
            return Response(serializer.data)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(
            categories, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, context={'request': request})
            return Response(serializer.data)

        except Category.DoesNotExist as ex:
            return Response({'message': 'Category does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        category = Category.objects.get(pk=pk)
        category.label = request.data['label']
        category.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for games
    Arguments:
        serializer type
    """
    class Meta:
        model = Category
        fields = ('id', 'label')