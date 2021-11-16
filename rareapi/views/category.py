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

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for games
    Arguments:
        serializer type
    """
    class Meta:
        model = Category
        fields = ('id', 'label')