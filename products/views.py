from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, File, Product
from .serializers import CategorySerializer, FileSerializer, ProductSerializer



class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context= {'request': request})
        return Response(serializer.data)
    

class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            products = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(products, context= {'request': request})
        return Response(serializer.data)

