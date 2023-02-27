from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, File, Product
from .serializers import CategorySerializer, FileSerializer, ProductSerializer


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)
    

class CategoryDetailView(APIView):
    def get(self, request, pk):
        try:
            categories = Product.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(categories, context={'request': request})
        return Response(serializer.data)





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
    


class FileListView(APIView):
    def get(self, request, product_id):
        files = File.objects.filter(product_id=product_id)
        serializer = FileSerializer(files, many=True, context={'request': request})
        return Response(serializer.data)
    

class FileDetailView(APIView):
    def get(self, request, pk, product_id):
        try:
            files = File.objects.get(pk=pk, product_id=product_id)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = FileSerializer(files, context= {'request': request})
        return Response(serializer.data)